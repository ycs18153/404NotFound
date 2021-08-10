# LINE CHATBOT
##### 主要是希望公司的 USER 除了用 TEAMS BOT 之外，在公司外也能透過 LINE 來查看待辦事項或收到待辦事項通知並無需額外的安裝，除了增加部署效益，也增加了便利性。
##### 主要功能有：待辦事項的查詢、新增、修改和刪除，疫情期間也提供可直接透過 Bot 來完成 `體溫回報表單`。
## File Structure
```
line_chatbot
├── Procfile
├── README.md
├── app.py
├── config.ini
├── magicMessage
│   ├── __pycache__
│   │   └── carousel.cpython-39.pyc
│   └── carousel.py
└── requirements.txt
```
* ##### app.py: USer 與 Bot 之間的介面，負責接收 User 請求，並將請求 Pass 給後端處理，最後將結果回應給 User。
* ##### Procfile: 將 BOT 部署至 Hroku 後，透過 Procfile 裡的指令來啟動 Bot。
* ##### magicMessage/carousel.py: 提供 Message Template。

## Deploy
> ##### 請先確認已經申請 Line Developer 帳號，並以創建一個開啟 Messaging API 的 Bot
### 本機部署(測試)

1. ##### 進入 config.ini，將 Channel Access Token 與 Channel Secret 改成自己 Bot 所提供的
```
[line-bot]
channel_access_token = {your_channel_access_token}
channel_secret = {your_channel_secret}
```
2. ##### 先安裝所需套件後，啟動 Bot
```
line_chartbot$ pip3 install -r requirements.txt
line_chartbot$ python3 app.py
```
3. ##### 再開另一台 Terminal，並透過 ngrok 取得一個暫時的對外 Address
```
$ ngrok http 5000
```
##### 複製 https 開頭的網址
![](https://i.imgur.com/qZZo5ki.png)

4. ##### 將剛剛複製的網址貼到 Line Bot 後台的 Webhook url 中，以開啟 Bot 與外界溝通的管道。

### Heroku 部署
> ##### 請先確保已經在 Heroku 上新增一個 App，並透過 git remote 指令將檔案與雲端專案連結。
##### 透過以下指令部署至 Heroku，push 成功後，Heroku 會去找我們的 Procfile ，透過 Procfile 內的指令來了解該如何啟動程式。
```
line_chatbot$ git add .
line_chatbot$ git commit -m "{your_commit_messages}"
line_chatbot$ git push heroku main
```

## 操作介紹
### Overview & Init
![](https://i.imgur.com/lemkSCT.png)

### 查看待辦事項
##### 點擊左下方按鈕來查看您的待辦事項
> ##### 若沒有待辦事項則會跳錯誤提醒，此情況為正常，將來當您有新增待辦事項後就可以正常使用
![](https://i.imgur.com/qf4occa.png)

### 刪除待辦事項
##### 在想要刪除之事項的卡片上按 Delete，即可將該筆資料刪除，成功刪除後將自動再推送更新過後的待辦事項集合。
![](https://i.imgur.com/1ssI5Fc.png)

### 新增與更新待辦事項
##### 由於 Line 官方無提供輸入資料的 Message Template，所以為了不讓 User 總是在訊息框按照我們的規定輸入資料，目前新增與更新待辦事項的功能我們透過 Line 官方提供的 liff 工具，將我們的 Web UI 嵌進 Line 的介面直接使用。如此能避免使用者的錯誤輸入，也增加了便利性。
![](https://i.imgur.com/U1YgKdb.png)

### 體溫回報表單
##### 疫情期間，提供體溫回報專區，讓你打開最熟悉的軟體做必須做的事。
![](https://i.imgur.com/W9b1xqb.png)
