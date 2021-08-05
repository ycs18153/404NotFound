# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys,os,time,threading
import traceback
from datetime import datetime
from typing import Dict
import asyncio

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
    ActivityHandler
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes, ConversationReference

from bot import MyBot
from config import DefaultConfig

global STOP


CONFIG = DefaultConfig()

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)
CONVERSATIONS_REFERENCE : Dict[str, ConversationReference] = dict()

# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error

# Create the Bot
BOT = MyBot(CONVERSATIONS_REFERENCE)

async def send_proactive_message():
    while True:
        # global stop_threads
        if STOP:
            break
        time.sleep(10)
        current_time = time.localtime()
        result = time.strftime("%I:%M:%S %p", current_time)
        print(result)
        if CONVERSATIONS_REFERENCE.keys():
            print("=====")
            for conversation in CONVERSATIONS_REFERENCE.values():
                await ADAPTER.continue_conversation(
                    conversation,
                    lambda turn_context : turn_context.send_activity(f"It is now {result}."),
                    CONFIG.APP_ID
                )

def target_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_proactive_message())


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
        print('=====')
        print(body)
        if body['text'] == 'stop':
            print(body['text'])
            STOP = True
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=201)



APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)



if __name__ == "__main__":

    STOP = False
    _thread = threading.Thread(target=target_callback)
    _thread.start()

    try:
        # web.run_app(APP, host="localhost", port=CONFIG.PORT)
        port = os.getenv('PORT', default=CONFIG.PORT)
        web.run_app(APP,port=port)
    except Exception as error:
        raise error
