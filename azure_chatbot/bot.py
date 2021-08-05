# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory# get_conversation_reference
from botbuilder.schema import ChannelAccount, HeroCard, CardAction, CardImage, ActionTypes, Attachment, Activity, ActivityTypes, ConversationReference
import requests
import json
import copy
from typing import Dict
from updateCard import *
from viewAllCard import *
from addTodoCard import *
from addOrUpdateResultCard import *
from myEhrCard import *
from deleteCard import *


def create_hero_card() -> Attachment:
    herocard = HeroCard(title="推薦以下兩個選項",
    images=[
        CardImage(
            url="https://ct.yimg.com/xd/api/res/1.2/VhPkyLMc5NAyXyGfjLgA5g--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD01ODU7cT04NTtyb3RhdGU9YXV0bzt3PTcwMA--/https://s.yimg.com/ob/image/82cbd7d4-5802-4b2b-99bd-690512b34730.jpg"
        )],  # https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg
    buttons=[
        CardAction(type=ActionTypes.open_url, title="url1",
                   value="https://www.google.com"),
        CardAction(type=ActionTypes.open_url, title="url2",
                   value="https://www.yahoo.com"),
        ])
    return CardFactory.hero_card(herocard)


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    contextToReturn = None
    def __init__(self, conversation: Dict[str, ConversationReference]):
        self.conver = conversation

    async def on_conversation_update_activity(self, turn_context: TurnContext):
        # if turn_context.activity.members_added[0].id != turn_context.activity.recipient.id:
        conversation = TurnContext.get_conversation_reference(turn_context.activity)
        self.conver[conversation.user.id] = conversation

        return await super().on_conversation_update_activity(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        # print('activity: ',json.dumps(turn_context.activity, sort_keys=True, indent=4),'\n')
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        conversation_id=TurnContext.get_conversation_reference(turn_context.activity).user.id
        self.conver[conversation_id] = TurnContext.get_conversation_reference(turn_context.activity)
        print('**************get converstion id**************\n',conversation_id)
        # print(get_conversation_reference(conversation_id))
        # print('**************get user id**************\n',(turn_context.activity).from.id)
        print('turn_context.activity:\n',turn_context.activity)
        if ('tenant' in turn_context.activity.channel_data.keys()):
            teams_tenantID=turn_context.activity.channel_data['tenant']['id']
        elif ('source' in turn_context.activity.channel_data.keys()):
            teams_tenantID=turn_context.activity.channel_data['source']['userId']
        else:
            teams_tenantID=turn_context.activity.channel_data['clientActivityID']
        print('teams_tenantID',teams_tenantID)

        if turn_context.activity.text != None:
            if turn_context.activity.text.startswith("工號_"):
                # TODO 連接 API
                # see mongo DB connect mongo db
                employee_id=turn_context.activity.text[3:]
                data={
                  "employee_id":employee_id,
                  "user_id":teams_tenantID
                }
                result=requests.post('https://tsmcbot-404notfound.du.r.appspot.com/api/employee-id',json=data)
                if result.status_code == requests.codes.ok:
                # response
                  contextToReturn = '恭喜您，添加成功! \n\n 請輸入 "help"，來查看更多服務\n\n 輸入"查看代辦事項"，查看代辦事項\n\n s輸入"新增代辦事項"，來新增TodoList\n\n  輸入"tsmc"，查看網頁的url'
                else:
                  contextToReturn ='工號添加失敗，請再嘗試一次或聯絡IT help desk'
            elif turn_context.activity.text == 'help':
                contextToReturn = '輸入"工號_XXXXXX  (舉例)工號_120734"，新增工號以方便連結 teams, line 及 web 的服務\n\n 輸入"查看代辦事項"，查看代辦事項\n\n 輸入"tsmc"，查看網頁的url\n\n 輸入"新增代辦事項"，新增代辦事項\n\n'
            elif '新增代辦事項' in turn_context.activity.text: #turn_context.activity.text == '新增代辦事項':
                contextToReturn = MessageFactory.attachment(Attachment(content_type='application/vnd.microsoft.card.adaptive',
                                        content=copy.deepcopy(addToDoListAdapCard)))
            elif turn_context.activity.text == 'tsmc':
                STOP = True
                contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareEhrCard()))
            # elif turn_context.activity.text == 'card':
            #     cardAtt = create_hero_card()
            #     contextToReturn = MessageFactory.attachment(cardAtt)
            # elif turn_context.activity.text == 'testMessage':
            #     contextToReturn = MessageFactory.text(
            #             "Welcome to CardBot. "
            #             + "This bot will show you different types of Rich Cards. "
            #             + "Please type anything to get started."
            #         )
            # elif turn_context.activity.text == 'adaptive':
            #     # contextToReturn =MessageFactory.attachment(Attachment(content_type='application/vnd.microsoft.card.adaptive',
            #     #                           content=adapCard))
            #     contextToReturn = MessageFactory.attachment(Attachment(
            #         content_type='application/vnd.microsoft.card.adaptive', content=testCard))
            elif '查看代辦事項' in turn_context.activity.text:#turn_context.activity.text == '查看代辦事項'
                # tasksInfo = [{"todo_id": "123123", "todo_name": "test1", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                # "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": True},
                #     {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                # "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False}]
                tasksInfo=requests.get(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s'%(teams_tenantID))
                if tasksInfo.status_code == requests.codes.ok:
                    # print('taskInfos\n',requests.get(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s'%(teams_tenantID)).content.decode('utf-8'))
                    tasksInfo=json.loads(tasksInfo.content.decode('utf-8'))
                    contextToReturn = MessageFactory.attachment(Attachment(
                        content_type='application/vnd.microsoft.card.adaptive', content=prepareViewAllCard(tasksInfo)))
                else:
                    contextToReturn ='目前沒有您的代辦事項，謝謝!!'
            else:
                contextToReturn = f"You said '{ turn_context.activity.text }'"
        elif turn_context.activity.value != None:
            if turn_context.activity.value['card_request_type']!=None:
                if turn_context.activity.value['card_request_type'] == 'submit_add':
                    print(type(turn_context.activity.value['start_time']))
                    # TODO 接到正確的API
                    my_data = {'todo_name': turn_context.activity.value['todo_name'],
                                'todo_date': turn_context.activity.value['start_date'].replace("-","/"),
                                'todo_contents': turn_context.activity.value['todo_contents'],
                                'todo_completed': turn_context.activity.value['todo_completed'],
                                'todo_update_date': turn_context.activity.timestamp.strftime("%Y/%m/%d"),
                                # 'employee_id': '120734'#turn_context.activity.channel_data['tenant']['id'],
                                }
                                # 'employee_id': turn_context.activity.channel_data['tenant']['id'],
                                # "line_user_id": turn_context.activity.channel_data['tenant']['id'],    #delete
                                # "teams_user_id": turn_context.activity.channel_data['tenant']['id']    #delete

                    # 將資料加入 POST 請求中
                    r = requests.post(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s'%(teams_tenantID), data = json.dumps(my_data))
                    if r.status_code == requests.codes.ok:
                        contextToReturn = '你已成功新增 %s 至代辦事項，下一步您可以透過查詢代辦事項來查看您的清單。' % (
                            turn_context.activity.value['todo_name'],)
                    else:
                        print(r.status_code)
                        print("Error: ", r.content)
                        contextToReturn = '請確認是否已經添加工號，如果問題持續發生，請聯絡系統管理員，謝謝'

                elif turn_context.activity.value['card_request_type'] == 'update_task':
                    data=turn_context.activity.value
                    print('data:\n',data)
                    # data["todo_date"]='2021-08-04 18:00'
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":data["todo_date"][:10],"start_time":data["todo_date"][11:],"todo_contents":data["todo_contents"],"todo_completed":data["todo_completed"]}
                    print('singletask:\n',singletask)
                    contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareUpdateCard(singletask)))

                elif turn_context.activity.value['card_request_type'] == 'delete_task':
                    data=turn_context.activity.value
                    singletask ={"todo_id":data["todo_id"]}
                    print('singletask:\n',singletask)
                    contextToReturn =MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content= deleteTask(singletask) ))

                elif turn_context.activity.value['card_request_type'] =='confirm_delete_task':
                    data=turn_context.activity.value
                    r=requests.delete(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s/%s'%(teams_tenantID,data["todo_id"]))#,json=singletask
                    print('delete response: ', r.status_code)
                    contextToReturn='Todo List 項目ID: '+data["todo_id"]+' 資料成功刪除'
                elif turn_context.activity.value['card_request_type'] =='cancel_delete_task':
                    data=turn_context.activity.value
                    contextToReturn='Todo List 項目ID: '+data["todo_id"]+' 資料未刪除'

                elif turn_context.activity.value['card_request_type'] == 'submit_update':
                    data=turn_context.activity.value
                    date_time=data["todo_date"]+' '+data["start_time"]
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":date_time,"todo_contents":data["todo_contents"],"todo_completed":data["todo_completed"]}
                    print('singletask:\n',singletask)
                    # call submit出去的API
                    requests.put(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s/%s'%(teams_tenantID,data["todo_id"]),json=singletask)
                    contextToReturn =MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=addOrUpdateResultCard(singletask)))
                    await turn_context.send_activity('Todo List 項目名稱＂'+data["todo_name"]+'＂已更新送出，祝 工作順心 ~ ')

        await turn_context.send_activity(contextToReturn)
        print()


    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("歡迎使用本機器人，請享受你在台積的時光。 \n\n "+
        "初次使用請輸入您的工號，以方便連結 teams, line 及 web 的服務\n\n 輸入格式(舉例):  工號_120734")
