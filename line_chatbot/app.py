from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage,
                            TextSendMessage, TemplateSendMessage, FlexSendMessage)
# from magicMessage import carousel
import configparser
import requests
import random
import json
import datetime
from requests.exceptions import SSLError
from magicMessage.carousel import todo, new_info, update_btn

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


helpMessage = "`create` to create a task.\n" \
    + "`read` to get all the tasks you created.\n" \
    + "`update <todo_id>` to update the content of the task.\n" \
    + "`delete <todo_id>` to remove the task.\n" \
    + "`get id` to get the task's ID for operations later."


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if "read" in event.message.text:
        try:
            response = requests.get(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}')
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=str(response.json())))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))

    elif "update" in event.message.text:
        try:
            todo_json = {
                'todo_contents': 'edit!'
            }
            todo_json = json.dumps(todo_json)
            response = requests.put(
                f'http://localhost:8000/api/todo/{event.source.user_id}/n9cJLY9jfl', todo_json)
            print(f'response: {response.json()}')
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))
    elif "delete" in event.message.text:
        try:
            todo_id = event.message.text.split(" ")[1].strip()
            requests.delete(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}/{todo_id}')
            response = requests.get(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}')
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=f'delete success!\n{str(response.json())}'))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))

    elif "create task" in event.message.text:
        try:
            todo_json = {
                "todo_name": "please",
                "todo_date": "2021-8-6",
                "todo_update_date": "2021-8-3",
            }
            todo_json = json.dumps(todo_json)
            requests.post("http://localhost:8000/api/todo/%s" % event.source.user_id,
                          todo_json)

            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="create success!"))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))
    elif "help" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=helpMessage))
    elif "test" in event.message.text:
        try:
            response = requests.get(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}')
            doc = response.json()
            card_title = ['Todo ID', 'Todo Title', 'Todo Date',
                          'Description', 'Update Date', 'Todo Status']
            card_value = ['todo_id', 'todo_name', 'todo_date',
                          'todo_contents', 'todo_update_date', 'todo_completed']
            # for each_record in doc:
            for i in range(6):
                new_info["contents"][0]["text"] = card_title[i]
                new_info["contents"][1]["text"] = doc[0]['todo_id']
                new_info_copy = new_info.copy()
                todo["body"]["contents"][2]["contents"].append(new_info_copy)

            line_bot_api.reply_message(event.reply_token, messages=FlexSendMessage(
                alt_text="測試訊息", contents=todo))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))


if __name__ == "__main__":
    app.run()
