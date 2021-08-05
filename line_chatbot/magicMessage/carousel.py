todo = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Your Todo List",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                    # insert six {new_info} here
                    # insert one {update_btn here}

                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "create",
                            "uri": "http://linecorp.com/"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "delete",
                            "uri": "http://linecorp.com/"
                        },
                        "style": "primary",
                        "margin": "10px"
                    }
                ]
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}

new_info = {
    "type": "box",
    "layout": "horizontal",
    "contents": [
        {
            "type": "text",
            "text": "Test",
            "size": "sm",
            "color": "#555555",
            "flex": 0
        },
        {
            "type": "text",
            "text": "QQQ",
            "size": "sm",
            "color": "#111111",
            "align": "end"
        }
    ]
}

update_btn = {
    "type": "button",
    "action": {
        "type": "message",
        "label": "update",
        "text": "update"
    },
    "height": "sm",
    "style": "secondary"
}

original = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Brown Store",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "conten ts": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Todo ID",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$2.99",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Todo Title",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$0.99",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Todo Date",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$3.33",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Description",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$7.31",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Update Date",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$8.0",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Todo Status",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$0.69",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "update",
                            "text": "update"
                        },
                        "height": "sm",
                        "style": "secondary"
                    }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "create",
                            "uri": "http://linecorp.com/"
                        },
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "delete",
                            "uri": "http://linecorp.com/"
                        },
                        "style": "primary",
                        "margin": "10px"
                    }
                ]
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
