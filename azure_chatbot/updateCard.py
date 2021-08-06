import copy
updateCard_oldver={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.0",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "Update Todo Task",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "Task_ID:  "+"12342151",
            "wrap": True,
            "id": "show_task_id",
            "separator": True,            
        },
        {
            "type": "TextBlock",
            "text": "Task Name",
            "wrap": True,
            "id": "task_name_label",
            "separator": True,
        },       
        {
            "type": "Input.Text",
            "style": "text",
            "id": "todo_name",
            "isRequired": True,
            "errorMessage": "Task name is required",
            "value": "Original_task_name",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "Task Start Date Time",
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "start_date",
            "value": "2021-08-01"
        },
        {
            "type": "Input.Time",
            "id": "start_time",
            "value": "16:59"
        },
        {
            "type": "TextBlock",
            "text": "Task End Date Time",
            "wrap": True,
            "id": "task_end_label",
            "separator": True,
        },             
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "End date for the task is required",
            "id": "end_date",
            "value": "2021-08-01"
        },
        {
            "type": "Input.Time",
            "id": "end_time",
            "value": "16:59"
        },
        {
            "type": "TextBlock",
            "text": "Task Contents",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            "id": "todo_contents"
        },
        {
            "type": "Input.Toggle",
            "title": "Task Complete",
            "value": "false",
            "id": "todo_completed",
            "separator": True,
        },
        {
            "type": "Container",
            "items": [
                {
                    "type": "ActionSet",
                    "horizontalAlignment": "Center",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "Submit",
                            "style": "positive",
                            "data": {
                                "card_request_type": "submit_update",
                                "task_id": "12342151",
                                "old_name":" "
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        
    ],
}

updateCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.0",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "更新代辦事項",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "項目_ID:  "+"12342151",
            "wrap": True,
            "id": "show_task_id",
            "separator": True,            
        },
        {
            "type": "TextBlock",
            "text": "項目名稱：",
            "wrap": True,
            "id": "task_name_label",
            "separator": True,
        },       
        {
            "type": "Input.Text",
            "style": "text",
            "id": "todo_name",
            "isRequired": True,
            "errorMessage": "Task name is required",
            "value": "Original_task_name",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "日期 / 時間：", 
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "todo_date",
            "value": "2021-08-01"
        },       
        {
        "type": "Input.ChoiceSet",
        "id": "start_time",
          "style": "compact",
          "isMultiSelect": "false",
          "value": "00:00",
          # "placeholder": "請輸入代辦事項時間",
          "choices": [
            {
              "title": "上午 12:00",
              "value": "00:00"
            },
            {
              "title": "上午 12:30",
              "value": "00:30"
            },
            {
              "title": "上午 01:00",
              "value": "01:00"
            },
            {
              "title": "上午 01:30",
              "value": "01:30"
            },
                        {
              "title": "上午 02:00",
              "value": "02:00"
            },
            {
              "title": "上午 02:30",
              "value": "02:30"
            },
                        {
              "title": "上午 03:00",
              "value": "03:00"
            },
            {
              "title": "上午 03:30",
              "value": "03:30"
            },
                        {
              "title": "上午 04:00",
              "value": "04:00"
            },
            {
              "title": "上午 04:30",
              "value": "04:30"
            },
                        {
              "title": "上午 05:00",
              "value": "05:00"
            },
            {
              "title": "上午 05:30",
              "value": "05:30"
            },
                        {
              "title": "上午 06:00",
              "value": "06:00"
            },
            {
              "title": "上午 06:30",
              "value": "06:30"
            },
                        {
              "title": "上午 07:00",
              "value": "07:00"
            },
            {
              "title": "上午 07:30",
              "value": "07:30"
            },
                        {
              "title": "上午 08:00",
              "value": "08:00"
            },
            {
              "title": "上午 08:30",
              "value": "08:30"
            },
                        {
              "title": "上午 09:00",
              "value": "09:00"
            },
            {
              "title": "上午 09:30",
              "value": "09:30"
            },
                        {
              "title": "上午 10:00",
              "value": "10:00"
            },
            {
              "title": "上午 10:30",
              "value": "10:30"
            },
                        {
              "title": "上午 11:00",
              "value": "11:00"
            },
            {
              "title": "上午 11:30",
              "value": "11:30"
            },
             {
              "title": "下午 12:00",
              "value": "12:00"
            },
            {
              "title": "下午 12:30",
              "value": "12:30"
            },
            {
              "title": "下午 01:00",
              "value": "13:00"
            },
            {
              "title": "下午 01:30",
              "value": "13:30"
            },
                        {
              "title": "下午 02:00",
              "value": "14:00"
            },
            {
              "title": "下午 02:30",
              "value": "14:30"
            },
                        {
              "title": "下午 03:00",
              "value": "15:00"
            },
            {
              "title": "下午 03:30",
              "value": "15:30"
            },
                        {
              "title": "下午 04:00",
              "value": "16:00"
            },
            {
              "title": "下午 04:30",
              "value": "16:30"
            },
                        {
              "title": "下午 05:00",
              "value": "17:00"
            },
            {
              "title": "下午 05:30",
              "value": "17:30"
            },
                        {
              "title": "下午 06:00",
              "value": "18:00"
            },
            {
              "title": "下午 06:30",
              "value": "18:30"
            },
                        {
              "title": "下午 07:00",
              "value": "19:00"
            },
            {
              "title": "下午 07:30",
              "value": "19:30"
            },
                        {
              "title": "下午 08:00",
              "value": "20:00"
            },
            {
              "title": "下午 08:30",
              "value": "20:30"
            },
                        {
              "title": "下午 09:00",
              "value": "21:00"
            },
            {
              "title": "下午 09:30",
              "value": "21:30"
            },
                        {
              "title": "下午 10:00",
              "value": "22:00"
            },
            {
              "title": "下午 10:30",
              "value": "22:30"
            },
                        {
              "title": "下午 11:00",
              "value": "23:00"
            },
            {
              "title": "下午 11:30",
              "value": "23:30"
            },

            ]
        },
        {
            "type": "TextBlock",
            "text": "Task End Date Time",
            "wrap": True,
            "id": "task_end_label",
            "separator": True,
            "isVisible": False
        },             
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "End date for the task is required",
            "id": "end_date",
            "value": "2021-08-01",
            "isVisible": False
        },
        {
            "type": "Input.Time",
            "id": "end_time",
            "value": "16:59",
            "isVisible": False
        },
        {
            "type": "TextBlock",
            "text": "項目內容及備註：",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            "id": "todo_contents"
        },
        {
            "type": "Input.Toggle",
            "title": "已完成",
            "value": False,
            "id": "todo_completed",
            "separator": True,
        },
        {
            "type": "Container",
            "items": [
                {
                    "type": "ActionSet",
                    "horizontalAlignment": "Center",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "送出更新",
                            "style": "positive",
                            "data": {
                                "card_request_type": "submit_update",
                                "todo_id": "12342151",
                                "old_name":" "
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        
    ],
}
def prepareUpdateCard(singletask={"todo_id":"123123","todo_name":"test1","todo_date":"2021-07-30",
                "start_time":"20:08","end_date":"2021-08-01",
                "end_time":"12:00","todo_contents":"contents,contents","todo_completed":False}):
    cardToReturn=copy.deepcopy(updateCard)    
    # singletask={"todo_id":"123123","todo_name":"test1","todo_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",
    #             "end_time":"12:00","todo_contents":"contents,contents","todo_completed":True}
    
    cardToReturn["body"][1]["text"]="項目_ID:  "+singletask["todo_id"]
    cardToReturn["body"][3]["value"]=singletask["todo_name"]
    cardToReturn["body"][5]["value"]=singletask["todo_date"]
    cardToReturn["body"][6]["value"]=singletask["start_time"] 
    cardToReturn["body"][11]["value"]=singletask["todo_contents"] if singletask["todo_contents"] else "   " 
    cardToReturn["body"][12]["value"]=True if singletask["todo_completed"] else False
    cardToReturn["body"][13]["items"][0]["actions"][0]["data"]["todo_id"]=singletask["todo_id"]
    # cardToReturn["body"][13]["items"][0]["actions"][0]["data"]["old_name"]=singletask["todo_id"]
    
    return cardToReturn

    
# prepareUpdateCard()