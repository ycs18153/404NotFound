# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory# get_conversation_reference
from botbuilder.schema import ChannelAccount, HeroCard, CardAction, CardImage, ActionTypes, Attachment, Activity, ActivityTypes
from botbuilder.schema.teams import TeamInfo, TeamsChannelAccount
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo
import requests
import json, copy,re
from cards.updateCard import *
from cards.viewAllCard import *
from cards.addTodoCard import *
from cards.addOrUpdateResultCard import *
from cards.myEhrCard import *
from cards.deleteCard import *
from cards.reminderCard import *


# def create_hero_card() -> Attachment:
#     herocard = HeroCard(title="推薦以下兩個選項",
#     images=[
#         CardImage(
#             url="https://ct.yimg.com/xd/api/res/1.2/VhPkyLMc5NAyXyGfjLgA5g--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD01ODU7cT04NTtyb3RhdGU9YXV0bzt3PTcwMA--/https://s.yimg.com/ob/image/82cbd7d4-5802-4b2b-99bd-690512b34730.jpg"
#         )],  # https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg
#     buttons=[
#         CardAction(type=ActionTypes.open_url, title="url1",
#                    value="https://www.google.com"),
#         CardAction(type=ActionTypes.open_url, title="url2",
#                    value="https://www.yahoo.com"),
#         ])
#     return CardFactory.hero_card(herocard)


class MyBot(ActivityHandler):
    contextToReturn = None

    async def on_message_activity(self, turn_context: TurnContext):
        print('turn_context.activity:\n',turn_context.activity)

        paged_members = []
        continuation_token = None       
        while True:
            current_page = await TeamsInfo.get_paged_members(
                turn_context, continuation_token, 100
            )
            continuation_token = current_page.continuation_token
            paged_members.extend(current_page.members)

            if continuation_token is None:
                break
        for m in paged_members: 
            print('paged_members:  ',m.as_dict())
        print()

        print('turn_context_from_property: \n',turn_context.activity.from_property.as_dict())        
        print('turn_context_conversation: \n',turn_context.activity.conversation.as_dict())
        print('turn_context_recipient: \n',turn_context.activity.recipient.as_dict())
        conversation_dict=turn_context.activity.conversation.as_dict()
        # try:
        #     member = await TeamsInfo.get_member(
        #         turn_context, turn_context.activity.from_property.id
        #     )
        # except Exception as e:
        #     if "MemberNotFoundInConversation" in e.args[0]:
        #         await turn_context.send_activity("Member not found.")
        #     else:
        #         raise
        # else:
        #     print('member: ',member)
        # print()
        
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        userid=TurnContext.get_conversation_reference(turn_context.activity).user.id
        print('**************get userid**************\n',userid)

        if turn_context.activity.text != None:
            regex=re.compile(r'工號_(\d+)')
            match=regex.search(turn_context.activity.text)
            # if turn_context.activity.text.startswith("工號_"):
            matchResult=match.group(1) if match else False
            if matchResult:
                # TODO 連接 API
                # see mongo DB connect mongo db
                # employee_id=turn_context.activity.text[3:]
                if "tenant_id" in conversation_dict.keys():
                    data={
                    "employee_id":matchResult,
                    "user_id":userid,#teams_tenantID
                    "tenant_id":conversation_dict["tenant_id"]
                    }
                else: 
                    data={
                    "employee_id":matchResult,
                    "user_id":userid
                    }
                print('data: ',data)
                result=requests.post('https://tsmcbot-404notfound.du.r.appspot.com/api/employee-id',json=data)
                print('result: ',result)
                if result.status_code == requests.codes.ok:
                # response
                  contextToReturn = '恭喜您，添加成功! \n\n 請輸入 "help"，來查看更多服務\n\n 輸入"查看代辦事項"，查看未完成的代辦事項\n\n 輸入"新增代辦事項"，來新增TodoList\n\n  輸入"tsmc"，查看網頁的url'
                else: 
                  contextToReturn ='工號添加失敗，請再嘗試一次或聯絡IT help desk'
            elif 'help' in turn_context.activity.text: #turn_context.activity.text == 'help':
                contextToReturn = '輸入"工號_XXXXXX  (舉例)工號_120734"，新增工號以方便連結 teams, line 及 web 的服務\n\n 輸入"查看代辦事項"，查看未完成的代辦事項\n\n 輸入"新增代辦事項"，新增代辦事項，新增之事項將於事件前大約15分鐘進行提醒\n\n 輸入"tsmc"，查看網頁的url\n\n'
            elif '新增代辦事項' in turn_context.activity.text: #turn_context.activity.text == '新增代辦事項':
                contextToReturn = MessageFactory.attachment(Attachment(content_type='application/vnd.microsoft.card.adaptive',
                                        content=copy.deepcopy(addToDoListAdapCard)))
            elif  'tsmc' in turn_context.activity.text:#turn_context.activity.text == 'tsmc':
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
            #     task={"todo_id": "123123", "todo_name": "test1", "todo_date": "2021-07-30 20:08", "todo_contents": "contents,contents contents,contents contents,contents contents,contents contents,contents", "todo_completed": True}
            #     contextToReturn = MessageFactory.attachment(Attachment(
            #         content_type='application/vnd.microsoft.card.adaptive', content=prepareReminderCard(task)))
            elif '查看代辦事項' in turn_context.activity.text:#turn_context.activity.text == '查看代辦事項'
                # tasksInfo = [{"todo_id": "123123", "todo_name": "test1", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                # "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": True},
                #     {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                # "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False}]
                tasksInfo=requests.get(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s'%(userid))
                if tasksInfo.status_code == requests.codes.ok:
                    tasksInfo=json.loads(tasksInfo.content.decode('utf-8'))
                    tasksInfoQueue=[tasksInfo[x:x+5] for x in range(0, len(tasksInfo),5)]
                    for item in tasksInfoQueue:
                        contextToReturn = MessageFactory.attachment(Attachment(
                            content_type='application/vnd.microsoft.card.adaptive', content=prepareViewAllCard(item)))
                        await turn_context.send_activity(contextToReturn)  
                    return                  
                else: 
                    contextToReturn ='目前沒有您的代辦事項，謝謝!!'
            else:
                contextToReturn = f"You said '{ turn_context.activity.text }'"
        elif turn_context.activity.value != None:
            if turn_context.activity.value['card_request_type']!=None:
                if turn_context.activity.value['card_request_type'] == 'submit_add': 
                    inputParams=turn_context.activity.value
                    if 'start_time' not in inputParams.keys() or 'start_date' not in inputParams.keys() or 'todo_name' not in inputParams.keys():
                        await turn_context.send_activity("新增失敗，請確認代辦事項之項目名稱、日期、時間是否填寫(不可為空值)。")
                        return
                    print(type(turn_context.activity.value['start_time']))
                    # TODO 接到正確的API
                    todoDate = turn_context.activity.value['start_date'] + " " + turn_context.activity.value['start_time']
                    print(todoDate)
                    my_data = {'todo_name': turn_context.activity.value['todo_name'], 
                                'todo_date': todoDate,
                                'todo_contents': turn_context.activity.value['todo_contents'] if 'todo_contents' in turn_context.activity.value.keys() else "   ",
                                'todo_completed': True if (turn_context.activity.value["todo_completed"]=='true') or (turn_context.activity.value["todo_completed"]==True) or (turn_context.activity.value["todo_completed"]=='True') else False,
                                'todo_update_date': turn_context.activity.timestamp.strftime("%Y/%m/%d"),
                                }

                    # 將資料加入 POST 請求中
                    r = requests.post(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s'%(userid), data = json.dumps(my_data))
                    if r.status_code == requests.codes.ok:
                        contextToReturn = '你已成功新增 "%s" 至代辦事項，下一步您可以透過 "查看代辦事項" 來查看您的清單。' % (
                            turn_context.activity.value['todo_name'],)
                    else: 
                        print(r.status_code)
                        print("Error: ", r.content)
                        contextToReturn = '請確認是否已經添加工號，以及代辦事項之項目名稱、日期、時間是否填寫(不可為空值)，如果問題持續發生，請聯絡系統管理員，謝謝'
                
                elif turn_context.activity.value['card_request_type'] == 'update_task':                
                    data=turn_context.activity.value
                    if 'todo_date' not in data.keys() or 'todo_name' not in data.keys():
                        await turn_context.send_activity("新增失敗，請確認代辦事項之項目名稱、日期、時間是否填寫(不可為空值)。")
                        return                    
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":data["todo_date"][:10],"start_time":data["todo_date"][11:19],"todo_contents":data["todo_contents"],"todo_completed":data["todo_completed"]}
                    print('singletask:\n',singletask)
                    contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareUpdateCard(singletask)))                  

                elif turn_context.activity.value['card_request_type'] == 'delete_task':                    
                    data=turn_context.activity.value
                    singletask ={"todo_id":data["todo_id"],"todo_name":data["todo_name"]}
                    print('singletask:\n',singletask)
                    contextToReturn =MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content= deleteTask(singletask) ))

                elif turn_context.activity.value['card_request_type'] =='confirm_delete_task':
                    data=turn_context.activity.value
                    r=requests.delete(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s/%s'%(userid,data["todo_id"]))#,json=singletask
                    print('delete response: ', r.status_code)
                    contextToReturn='Todo List 項目ID: '+data["todo_id"]+' 資料成功刪除'
                    
                elif turn_context.activity.value['card_request_type'] =='cancel_delete_task':
                    data=turn_context.activity.value
                    contextToReturn='Todo List 項目ID: '+data["todo_id"]+' 資料未刪除'
                        
                elif turn_context.activity.value['card_request_type'] == 'submit_update':
                    data=turn_context.activity.value
                    print("submit_update data:",data)
                    date_time=data["todo_date"]+' '+data["start_time"] if "start_time" in data.keys() else data["todo_date"]+' '+"00:00"
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":date_time,"todo_contents":data["todo_contents"],
                    "todo_completed":True if (data["todo_completed"]=='true') or (data["todo_completed"]==True) or (data["todo_completed"]=='True') else False}
                    requests.put(f'https://tsmcbot-404notfound.du.r.appspot.com/api/todo/%s/%s'%(userid,data["todo_id"]),json=singletask)
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
