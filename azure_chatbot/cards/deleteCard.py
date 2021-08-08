import copy

deleteCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "預計刪除資料如下",
            "wrap": True,
            "horizontalAlignment": "Center"
        },
        {
            "type": "FactSet",
            "separator": True, 
            "facts": [
                {
                    "title": "項目 ID",
                    "value": "12342151"
                },
                {
                    "title": "項目名稱",
                    "value": "making cards"
                }
            ]
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
                                "title": "刪除",
                                "data": {
                                    "card_request_type": "confirm_delete_task"
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
                                "title": "取消",
                                "data": {
                                    "card_request_type": "cancel_delete_task"
                                }
                            }
                        ]
                    }
                ]
            }
        ]}
    ]
}

def deleteTask(singletask):
    print('*****************singletask:*****************\n',singletask)
    cardToReturn=copy.deepcopy(deleteCard)
    cardToReturn["body"][1]["facts"][0]["value"]=singletask["todo_id"]
    cardToReturn["body"][1]["facts"][1]["value"]=singletask["todo_name"]

    # cardToReturn["body"][2]["columns"][0]["items"][0]["actions"][0]["data"].update(singletask)
    # cardToReturn["body"][2]["columns"][1]["items"][0]["actions"][0]["data"].update(singletask)
    cardToReturn["body"][2]["columns"][0]["items"][0]["actions"][0]["data"]["todo_id"]=singletask["todo_id"]
    cardToReturn["body"][2]["columns"][1]["items"][0]["actions"][0]["data"]["todo_id"]=singletask["todo_id"]   
    print('===========confirm delete card: ===============\n', cardToReturn)

    return cardToReturn