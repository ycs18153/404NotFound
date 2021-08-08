from __future__ import unicode_literals
import os
import re
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage,
                            TextSendMessage, TemplateSendMessage, FlexSendMessage, ConfirmTemplate, URIAction, MessageAction, PostbackEvent)
import configparser
from linebot.models.events import Postback
import requests
import random
import json
import logging
import datetime
import copy
from requests.api import delete
from requests.exceptions import SSLError
from magicMessage.carousel import todo, new_info

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


@handler.add(PostbackEvent)
def postbackReply(event):
    data = event.postback.data
    print(data)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if "工號_" in event.message.text:
        employee_id = event.message.text.split("_")[1].strip()
        payload = {
            "employee_id": employee_id,
            "user_id": event.source.user_id
        }
        response = requests.post(
            f'https://tsmcbot-404notfound.du.r.appspot.com/api/employee-id', payload, timeout=5)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=f'add user success! Now you can do `CRUD` operations'))

    elif "read" in event.message.text:
        try:
            response = requests.get(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}', timeout=5)
            each_todo = response.json()
            todo_copy = add_carousel(each_todo)
            message = FlexSendMessage(alt_text="todo list", contents=todo_copy)
            line_bot_api.reply_message(event.reply_token, message)

        except Exception as e:
            logging.error('Error Msg: ',  exc_info=e)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))

    elif "delete" in event.message.text:
        try:
            print("delete!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            todo_id = event.message.text.split(" ")[1].strip()
            requests.delete(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}/{todo_id}', timeout=5)
            response = requests.get(
                f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/{event.source.user_id}', timeout=5)
            each_todo = response.json()
            todo_copy = add_carousel(each_todo)
            message = FlexSendMessage(alt_text="todo list", contents=todo_copy)
            line_bot_api.push_message(
                event.source.user_id, TextSendMessage(text='Delete success!'))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="something wents wrong, please retry..."))


def add_carousel(each_todo):

    todo_copy = {}
    todo_copy = copy.deepcopy(todo)

    for i in range(len(each_todo)):
        new_info_copy = {}
        new_info_copy = copy.deepcopy(new_info)
        new_info_copy["header"]["contents"][1]["text"] = each_todo[i]["todo_id"]
        new_info_copy["body"]["contents"][0]["contents"][1]["text"] = each_todo[i]["todo_name"]
        new_info_copy["body"]["contents"][1]["contents"][1]["text"] = each_todo[i]["todo_date"][5:10] + \
            " "+each_todo[i]["todo_date"][11:16]
        new_info_copy["body"]["contents"][2]["contents"][1]["text"] = each_todo[i]["todo_contents"]
        new_info_copy["body"]["contents"][3]["contents"][1]["text"] = str(
            each_todo[i]["todo_update_date"])
        new_info_copy["body"]["contents"][4]["contents"][1]["text"] = str(
            each_todo[i]["todo_completed"])
        new_info_copy["footer"]["contents"][1]["action"]["data"] = each_todo[i]["todo_id"]
        new_info_copy["footer"]["contents"][1]["action"][
            "text"] = f'delete {each_todo[i]["todo_id"]}'
        todo_copy["contents"].append(new_info_copy)
    return todo_copy


if __name__ == "__main__":
    app.run()
