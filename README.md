# 菜積別怕
##### HACKATHON PROJECT BY GROUP G (404 NOT FOUND)
> ##### MENTOR: 林聖凱
> ##### GROUP MEMBERS: 林哲偉 黃懿 林培權 吳德瑋 顏煥勳 姚瀚宇

## Description
##### 一進公司其實馬上就開始了一段充實的生活，有主管Assign的任務、要上必修的線上課程、要參加BootCamp活動，疫情期間要填溫度表單、要申請WFH、開發機要申請RDP等等，最後還有Hackathon Competition...
##### 當事情一多，很容易忘記待會可能還有個會要開，或是忘記原本安排給自己的任務等等。要解決這些問題的方法很多，你可以用Google Canlendar或其他行事曆來提醒你，但在公司你只能用Outlook或寫在紙上，但Outlook對剛出社會的學生來說相對不友善，所以我們打算為台積的菜鳥們打造一個專屬的解決方案。
##### 為了不再讓菜雞們
> 1. ##### 因為手邊沒熟悉的工具而又忘記了公司重要的事
> 2. ##### 在雜亂的信箱中翻找會議或活動時間
> 3. ##### 在面對公司提供的眾多服務中，找不到自己需要的網站 (我就不知道RDP要去哪裡申請QQ)
##### 我們希望能幫這些粗心大意的人紀錄待辦事項，並在期限快到的時候主動通知他們，此外，也提供了查詢公司服務網站的功能。

##### 由於在公司中最常使用到的軟體為Teams，為了降低將來的部署成本，本組採用Chat bot作為與User溝通的介面來達到以上目標。除了建構 ***Teams bot*** 之外，我們也提供了 ***Line bot*** 與 ***Web*** 介面，使菜雞們在公司外用Line或用Browser都能使用我們的服務。

## How To Use 
##### 請遵循Bot指示，當個好User乖乖使用，也請勿對Web進行XSS之類的攻擊。
1. #### Teams Bot: [按我即可加好友](https://teams.microsoft.com/l/chat/0/0?users=28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f)
2. #### Web: [點我進入](https://tsmc-todolist.de.r.appspot.com/)
3. #### Line Bot: 請掃QR Code
![](https://i.imgur.com/whsUhBP.png)


## Architecture
![](https://i.imgur.com/lzJ34uG.jpg)
##### 

## Services

* #### 透過與Bot互動來新增、刪除、修改或查詢重要的待辦事項
* #### 透過Bot的導引和說明來找到公司內部某服務的入口網站
* #### 主動通知你即將到來的待辦事項們，讓你想粗心都難
* #### 在公司內用Teams，公司外用Line或Web，都能使用服務

## File Structure
```
404NotFound
├── Procfile
├── README.md
├── azure_chatbot
│   ├── Procfile
│   ├── README.md
│   ├── __init__.py
│   ├── app.py
│   ├── app.yaml
│   ├── bot.py
│   ├── cards
│   │   ├── __init__.py
│   │   ├── addOrUpdateResultCard.py
│   │   ├── addTodoCard.py
│   │   ├── deleteCard.py
│   │   ├── myEhrCard.py
│   │   ├── reminderCard.py
│   │   ├── updateCard.py
│   │   ├── viewAllCard.py
│   │   └── winnie.jpg
│   ├── config.py
│   ├── deploymentTemplates
│   │   ├── template-with-new-rg.json
│   │   └── template-with-preexisting-rg.json
│   ├── index.html
│   ├── requirements.txt
│   ├── test.py
│   ├── test2.py
│   └── winnie.jpg
├── backend
│   ├── Procfile
│   ├── README.md
│   ├── __pycache__
│   │   ├── controller.cpython-37.pyc
│   │   ├── controller.cpython-38.pyc
│   │   ├── controller.cpython-39.pyc
│   │   ├── main.cpython-37.pyc
│   │   ├── main.cpython-38.pyc
│   │   ├── main.cpython-39.pyc
│   │   ├── model.cpython-37.pyc
│   │   ├── model.cpython-38.pyc
│   │   └── model.cpython-39.pyc
│   ├── app.yaml
│   ├── config
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-37.pyc
│   │       ├── __init__.cpython-38.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── controller.py
│   ├── main.py
│   ├── model.py
│   └── requirements.txt
├── cronjob
│   ├── proactive_message.py
│   ├── readme.md
│   └── requirements.txt
├── frontend
│   ├── README.md
│   ├── images
│   │   ├── add_1.png
│   │   ├── add_2.png
│   │   ├── delete.png
│   │   ├── login_1.png
│   │   ├── login_2.png
│   │   └── modify.png
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   └── src
│       ├── Switch.jsx
│       ├── index.css
│       ├── index.js
│       └── pages
│           ├── Home
│           │   ├── api
│           │   │   └── Api.js
│           │   ├── components
│           │   │   ├── Edit.js
│           │   │   ├── Item.js
│           │   │   ├── List.js
│           │   │   └── Loader
│           │   │       ├── Loader.css
│           │   │       └── Loader.jsx
│           │   ├── index.css
│           │   └── index.jsx
│           └── Login
│               ├── index.css
│               └── index.jsx
├── img
│   ├── auto_gen_docs.PNG
│   ├── cron_dashboard.PNG
│   ├── cron_pubsub.PNG
│   ├── cron_trigger.PNG
│   ├── head.PNG
│   ├── mongo_ToDo.PNG
│   ├── mongo_collection.PNG
│   ├── mongo_create_db.PNG
│   ├── mongo_docker.PNG
│   ├── mongo_gcp.PNG
│   ├── mongo_get.PNG
│   └── start.PNG
├── line_chatbot
│   ├── Procfile
│   ├── README.md
│   ├── app.py
│   ├── config.ini
│   ├── magicMessage
│   │   ├── __pycache__
│   │   │   └── carousel.cpython-39.pyc
│   │   └── carousel.py
│   └── requirements.txt
├── mongodb
│   ├── docker-compose.yaml
│   └── readme.md
└── tree.text

23 directories, 98 files

```
