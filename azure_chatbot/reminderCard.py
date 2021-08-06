import os, base64,copy,requests
file = os.path.join(os.getcwd(), "winnie.jpg")
image = open(file, 'rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read).decode()

contentContainer={
  "contentType": "application/vnd.microsoft.card.adaptive",
  "content": ""}
reminderTemplate={
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.0",
  "body": [
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "事項提醒",
          "weight": "bolder",
          "size": "medium"
        },
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "Image",
                  "url": f"data:image/jpg;base64,{image_64_encode}",
                  "size": "small",
                  "style": "person"
                }
              ]
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "維尼 (虛擬助手)",
                  "weight": "bolder",
                  "wrap": True
                },
                {
                  "type": "TextBlock",
                  "spacing": "none",
                  "text": "Created {{DATE(2021-08-01T06:08:39Z, SHORT)}}",
                  "isSubtle": True,
                  "wrap": True,
                  "isVisible": False
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "提醒您，您的活動 / 事項：_______________即將開始。",
          "wrap": True
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.ShowCard",
      "title": "檢視即將到來事項",
      "card": {
        "type": "AdaptiveCard",
        "body": [{
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
                },
            ],
            # "separator": True
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
    }
  ]
}

def prepareReminderCard(taskToRemind):
    reminderCard=copy.deepcopy(reminderTemplate) #20字以上換行
    reminderCard["body"][1]["items"][0]["text"]="提醒您，您的活動 / 事項： "+taskToRemind["todo_name"]+" 即將開始。"
    reminderCard["actions"][0]["card"]["body"][0]["facts"][0]["value"]=taskToRemind["todo_id"]
    reminderCard["actions"][0]["card"]["body"][0]["facts"][1]["value"]=taskToRemind["todo_name"]
    reminderCard["actions"][0]["card"]["body"][0]["facts"][2]["value"]=taskToRemind["todo_date"]
    reminderCard["actions"][0]["card"]["body"][0]["facts"][3]["value"]="True" if taskToRemind["todo_completed"] else"False"
    if taskToRemind["todo_contents"]:
      if len(taskToRemind["todo_contents"])<=21: 
        reminderCard["actions"][0]["card"]["body"][0]["facts"][4]["value"]=taskToRemind["todo_contents"]
      else: 
        reminderCard["actions"][0]["card"]["body"][1]["text"]=taskToRemind["todo_contents"]
        reminderCard["actions"][0]["card"]["body"][1]["isVisible"]=True
        reminderCard["actions"][0]["card"]["body"][0]["facts"][4]["value"]=" "
    container=copy.deepcopy(contentContainer)
    container["content"]=reminderCard
    return container
  
# accessTokenUrl='https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'


