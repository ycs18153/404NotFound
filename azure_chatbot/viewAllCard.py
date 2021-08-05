import copy

viewAllCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "所有事項",
            "wrap": True,
            "horizontalAlignment": "Center"
        },

    ]
}

singleTask= [{
            "type": "FactSet",
            "facts": [
                {
                    "title": "項目 ID",
                    "value": "12342151"
                },
                {
                    "title": "項目名稱",
                    "value": "making cards"
                },
                {
                    "title": "項目日期",
                    "value": "2021-07-31"
                },                        
                {
                    "title": "完成",
                    "value": "False"
                },                
                {
                    "title": "項目內容及備註",
                    "value": "xxxtask contentsxxx"  
                }
            ],
            "separator": True
        },
        {
            "type": "TextBlock",
            "text": "項目內容備註內容",
            "wrap": True,
            "id": "task contents__for long contents",
            "separator": True,
            "isVisible":False    
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": "stretch",
                    "items": [
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "更新項目",
                                    "data": {
                                        "card_request_type": "update_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": "stretch",
                    "items": [
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "刪除項目",
                                    "data": {
                                        "card_request_type": "delete_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }]

singleTask_old= [{
            "type": "FactSet",
            "facts": [
                {
                    "title": "項目 ID",
                    "value": "12342151"
                },
                {
                    "title": "項目名稱",
                    "value": "making cards"
                },
                {
                    "title": "日期",
                    "value": "2021-07-31"
                },
                {
                    "title": "時間",
                    "value": "21:00",
                    "isVisible": False
                },                
                {
                    "title": "End Date",
                    "value": "2021-08-01",
                    "isVisible": False
                },
                {
                    "title": "End Time",
                    "value": "21:00",
                    "isVisible": False
                },                        
                {
                    "title": "完成",
                    "value": "False"
                },        
                {
                    "title": "項目內容及備註",
                    "value": "xxxtask contentsxxx"  
                }
            ],
            "separator": True
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": "stretch",
                    "items": [
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "Update Task",
                                    "data": {
                                        "card_request_type": "update_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": "stretch",
                    "items": [
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "Delete Task",
                                    "data": {
                                        "card_request_type": "delete_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }]

def prepareViewAllCardTest():
    cardReturn=copy.deepcopy(viewAllCard)
    task=copy.deepcopy(singleTask)
    cardReturn["body"]=cardReturn["body"]+task+task
    return cardReturn

# [{"todo_id":"123123","todo_name":"test1","start_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",\
#               "end_time":"12:00","todo_contents":"contents,contents","todo_completed":True},\
#  {"todo_id":"321321","todo_name":"test2","start_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",\
#               "end_time":"12:00","todo_contents":"contents,contents","todo_completed":False}]
def prepareViewAllCard(taskInfos):
    cardReturn=copy.deepcopy(viewAllCard)

    for task in taskInfos:    
        task_template=copy.deepcopy(singleTask)
        print('task\n',task)
        task_template[0]["facts"][0]["value"]=task["todo_id"]
        task_template[0]["facts"][1]["value"]=task["todo_name"]
        task_template[0]["facts"][2]["value"]=task["todo_date"]  #task["start_date"]
        # task_template[0]["facts"][3]["value"]=task["start_time"]      
        # task_template[0]["facts"][4]["value"]=task["end_date"] 
        # task_template[0]["facts"][5]["value"]=task["end_time"]
        task_template[0]["facts"][3]["value"]=task["todo_completed"]  
        if len(task["todo_contents"])<=21:                            
            task_template[0]["facts"][4]["value"]=task["todo_contents"]
        else:
            task_template[0]["facts"][4]["value"]=" "
            task_template[1]["text"]=task["todo_contents"]
            task_template[1]["isVisible"]=True
        task_template[2]["columns"][0]["items"][0]["actions"][0]["data"].update(task)
        task_template[2]["columns"][1]["items"][0]["actions"][0]["data"].update(task)
        
        cardReturn["body"]=cardReturn["body"]+task_template      
        
    return cardReturn

