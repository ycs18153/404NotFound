import copy

presentCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "項目狀態更新如下",
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
                },
                {
                    "title": "日期時間",
                    "value": "2021-07-31"
                },                        
                {
                    "title": "已完成",
                    "value": False
                },                
                {
                    "title": "項目內容及備註",
                    "value": "xxxtask contentsxxx"  
                }
            ]
        },                
        {
        "type": "TextBlock",
        "text": "項目內容備註內容",
        "wrap": True,
        "id": "task contents__for long contents",
        "separator": True,
        "isVisible":False
        }
    ]
}

def addOrUpdateResultCard(singletask):
    cardToReturn=copy.deepcopy(presentCard)
    cardToReturn["body"][1]["facts"][0]["value"]=singletask["todo_id"]
    cardToReturn["body"][1]["facts"][1]["value"]=singletask["todo_name"]
    cardToReturn["body"][1]["facts"][2]["value"]=singletask["todo_date"]
    cardToReturn["body"][1]["facts"][3]["value"]=True if (singletask["todo_completed"]=='true') or (singletask["todo_completed"]==True) or (singletask["todo_completed"]=='True') else False
    cardToReturn["body"][1]["facts"][4]["value"]=singletask["todo_contents"]    
    if singletask["todo_contents"]:
      if len(singletask["todo_contents"])<=21: 
        cardToReturn["body"][1]["facts"][4]["value"]=singletask["todo_contents"]
      else: 
        cardToReturn["body"][2]["text"]=singletask["todo_contents"]
        cardToReturn["body"][2]["isVisible"]=True
        cardToReturn["body"][1]["facts"][4]["value"]=" "    
    
    return cardToReturn