# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys,os,json,requests,copy,logging
import traceback
from datetime import datetime


from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes

from bot import MyBot
from config import DefaultConfig
from reminderCard import prepareReminderCard

CONFIG = DefaultConfig()

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


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
BOT = MyBot()


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=415)
    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=201)

routes = web.RouteTableDef()
@routes.post('/api/v1/cron-messages')
async def sendReminder(request):
    try:
        todoInfo = await request.json()  # suppose a dict now    
        # {'tenant_id': '98fb227d-9ccb-46af-bbc7-7adfb3090fa6', 
        # 'user_id': '29:1EHxt_msQczs0jFpTh3HUdDzzbQhOQLsins3m8VHWjctZ2DF7Htq-89Dmv3T-t6KhnJxn2uzoNL1r5qNEu3myiQ', 
        # 'todo':  {'todo_id': 'Gq31ES4ipg', 'todo_name': 'test_cronjob', 
        # 'todo_date': datetime.datetime(2021, 8, 6, 2, 0), 
        # 'todo_contents': 'test_cronjob', 'todo_update_date': '2021/08/05', 
        # 'todo_completed': False, 'employee_id': '109491'}}
        teams_appid='30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
        appSecret='ElizaHuangTaigidian2021'
        botId='28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
        userId=todoInfo['user_id']    
        tenant_id=todoInfo['tenant_id']
        cardToSend=prepareReminderCard(todoInfo["todo"])
        ## access token
        url='https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'
        payload = {'Host': 'login.microsoftonline.com',
            "Content-Type": "application/x-www-form-urlencoded",
            'grant_type':'client_credentials',
            'client_id':teams_appid,
            'client_secret':appSecret,
            'scope':'https://api.botframework.com/.default'}
        
        r=requests.post(url, data=(payload))
        response=json.loads(r.content.decode('utf-8'))  
        access_token=response['access_token']  
        print('access_token:\n',access_token) 
        
        ## get conversationId
        header={'Authorization': 'Bearer ' + access_token} #, 'content-type':'application/json'
        url=f'https://smba.trafficmanager.net/apac/v3/conversations'
        payload={
            "bot": {
                "id": botId,#30eba4f2-6e15-458b-9fdf-f8bbf25efb4f
                # "name": "AzureBot001_Regis"
            },
            "isGroup": False,
            "members": [
                {
                    "id": userId, #usesrid_office,
                    "name":"" #"Yi Huang 黃懿"
                }
            ],
            "tenantId": tenant_id,
            "topicName": "proactive msg"
        }
        conversation_response=json.loads(requests.post(url,json=(payload), headers=header).content.decode('utf-8'))
        conversation_id=conversation_response["id"]
        print('conversation_id: \n',conversation_id)

        url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversation_id)
        payload_template={
            "type": "message",
            "from": {
                "id": botId,
                "name": "AzureBot001_Regis"
            },
            "conversation": {
                "id": conversation_id,
                "name": "send proactive msg now"
            },
            "recipient": {
                "id": userId,
                "name":"",# "Yi Huang 黃懿"
            },
            "attachments": []
        }
        payload=copy.deepcopy(payload_template)
        payload["attachments"]+=[cardToSend]
        response_forSendMsg =requests.post(url, json=(payload), headers=header).content.decode('utf-8')
        print('response_forSendMsg',response_forSendMsg)
        
        return Response(status=200)
    
    except Exception as e:
        logging.error('Error Msg: ',  exc_info=e)
        return Response(status=500)
    


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)
APP.add_routes(routes)
# APP.router.add_post("/api/v1/cron-messages",sendReminder)


if __name__ == "__main__":
    try:
        # web.run_app(APP, host="localhost", port=CONFIG.PORT)
        port = os.getenv('PORT', default=CONFIG.PORT)
        web.run_app(APP,port=port)
    except Exception as error:
        raise error
