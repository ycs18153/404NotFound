import os, base64
file = os.path.join(os.getcwd(), "winnie.jpg")
image = open(file, 'rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read).decode()

addToDoListAdapCard={
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.0",
  "body": [
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "代辦事項清單服務",
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
                  "url": f"data:image/jpg;base64,{image_64_encode}",#"https://img.ltn.com.tw/Upload/ent/page/800/2015/11/06/1500206_1.jpg",
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
          "text": "歡迎使用代辦事項服務，點選下列按鈕開始使用相關功能。",
          "wrap": True
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.ShowCard",
      "title": "添加新的代辦事項",
      "card": {
        "type": "AdaptiveCard",
        "body": [
          {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "添加新的代辦事項",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        # {
            # "type": "TextBlock",
            # "text": "Task_ID:  "+"12342151",
            # "wrap": True,
            # "id": "show_task_id",
            # "separator": True,            
        # },
        {
            "type": "TextBlock",
            "text": "代辦事項",
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
            "placeholder": "請輸入代辦事項名稱",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "代辦事項日期與時間",
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "start_date",
            "placeholder": "請輸入代辦事項日期"
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
        
        # {
            # "type": "Input.Time",
            # "id": "start_time",
            # "placeholder": "請輸入代辦事項時間",
        # },
        # {
            # "type": "TextBlock",
            # "text": "Task End Date Time",
            # "wrap": True,
            # "id": "task_end_label",
            # "separator": True,
        # },             
        # {
            # "type": "Input.Date",
            # "isRequired": True,
            # "errorMessage": "End date for the task is required",
            # "id": "end_date",
            # "value": "2021-08-01"
        # },
        # {
            # "type": "Input.Time",
            # "id": "end_time",
            # "value": "16:59"
        # },
        {
            "type": "TextBlock",
            "text": "代辦事項內容",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            # "placeholder": "請輸入代辦事項內容",
            "id": "todo_contents",
            "value": "    "
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
                                "card_request_type": "submit_add",
                                # "task_id": "12342151"
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        ],
        # "actions": [
          # {
            # "type": "Action.Submit",
            # "title": "OK",
            # "data": {
            # "card_type": "addToDoList"
          # }
          # }
        # ]
      }
    }
  ]
}

def prepareAddToDoListAdapCard():
    cardReturn=copy.deepcopy(addToDoListAdapCard)
    return cardReturn