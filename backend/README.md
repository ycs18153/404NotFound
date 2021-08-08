# Backend Server
##### 實作 FAST API 提供給呼叫，並負責與 ATLAS 上的 MONGODB 叢集溝通，使前端可對資料進行 CRUD 操作。

## File Structure
```
backend
│   README.md
│   requirements.txt
|   model.py
|   main.py
|   controller.py
|   app.yaml
|   Procfile
│
└───config
│   │   __init__.py
│   │   ...
│   
└───__pycache__
    │   ...
    |   ...
```
* ##### main.py: Backend 主程式，定義 API 形式提供給前端使用，並將前端請求 pass 給 controller 對資料庫進行操作。
* ##### controller.py: 負責對 DB 進行 CRUD 操作。
* ##### model.py: 定義所需要的資料型態。
* ##### app.yaml: 當部署上 GCP 後，透過此指令啟動 SERVER。
* ##### __init__.py: 與後端與資料庫連線的設定。
###### 其他略

## 本機測試
```
$ pip3 install -r requirements.txt 
$ uvicorn main:app --reload
```

## GCP 部署
##### 新增專案後進入 Cloud Shell ，先創建一個虛擬環境試 Work。
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

##### 測試過後，透過下列指令將 Backend 部署。
```
gcloud app create
gcloud app deploy app.yaml
gcloud app deploy app.yaml --project tsmc-bot
gcloud app browse
```