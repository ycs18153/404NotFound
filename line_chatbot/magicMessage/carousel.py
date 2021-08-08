todo = {
    "type": "carousel",
    "contents": [

    ]
}

new_info = {
    "type": "bubble",
    "size": "kilo",
    "header": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
            {
                "type": "text",
                "text": "Todo ID:",
                "color": "#ffffff",
                "align": "start",
                "size": "md",
                "gravity": "center"
            },
            {
                "type": "text",
                "text": "",
                "align": "start",
            }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Title"
                    },
                    {
                        "type": "text",
                        "text": "",
                        "color": "#8C8C8C",
                        "size": "sm",
                        "align": "end",
                        "wrap": True
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "When"
                    },
                    {
                        "type": "text",
                        "text": "",
                        "size": "sm",
                        "align": "end",
                        "color": "#8C8C8C",
                        "wrap": True
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Description"
                    },
                    {
                        "type": "text",
                        "text": "",
                        "size": "sm",
                        "align": "end",
                        "color": "#8C8C8C",
                        "wrap": True
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Create Date"
                    },
                    {
                        "type": "text",
                        "text": "",
                        "size": "sm",
                        "align": "end",
                        "color": "#8C8C8C"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Status"
                    },
                    {
                        "type": "text",
                        "text": "",
                        "size": "sm",
                        "align": "end",
                        "color": "#8C8C8C"
                    }
                ]
            }
        ],
        "spacing": "md",
        "paddingAll": "12px"
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "uri",
                    "label": "Update",
                    "uri": "https://liff.line.me/1656294870-YzrJDAmr"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "Delete",
                    "text": ""
                }
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": False
        }
    }
}
