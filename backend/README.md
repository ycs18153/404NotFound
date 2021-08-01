## Setup tutorial
##### Please run the following command to setup the backend server:
```
uvicorn main:app --reload
```

### GCP
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

gcloud app create
gcloud app deploy app.yaml
gcloud app deploy app.yaml --project tsmc-bot
gcloud app browse
```