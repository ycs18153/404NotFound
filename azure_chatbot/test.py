import requests,json
from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
# result=requests.get('https://tsmcbot-404notfound.du.r.appspot.com/api/myehr').content
# print(result)


url='https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'


payload = {'Host': 'login.microsoftonline.com',
    "Content-Type": "application/x-www-form-urlencoded",
    'grant_type':'client_credentials',
    'client_id':'30eba4f2-6e15-458b-9fdf-f8bbf25efb4f',
    'client_secret':'ElizaHuangTaigidian2021',
    'scope':'https://api.botframework.com/.default'}
# Host: login.microsoftonline.com
# Content-Type: application/x-www-form-urlencoded

# grant_type=client_credentials&client_id=MICROSOFT-APP-ID&client_secret=MICROSOFT-APP-PASSWORD&scope=https%3A%2F%2Fapi.botframework.com%2F.default
headers = {}# 
r = requests.post(url, data=(payload), headers=headers)# data=json.dumps(payload)
response=json.loads(r.content.decode('utf-8'))
print('access_token response:\n',response)
print('type: ',type(response))
access_token_dict=response
access_token=response['access_token']

# url='https://api.botframework.com'#https://smba.trafficmanager.net/apis/v3/conversations/12345/activities
# header={'Authorization': 'Bearer ' + access_token}
# response2=json.loads(r.content.decode('utf-8'))
# print('JWT token response:\n',response2)

channel_id='msteams'

'''try to get conversation id'''
userId='29:1lNWDIz8Jn0YgoFx8LTJWrkqchAJb1Vg0bJK-PvHxe2FHzNXzFHYaeA0P9j58qQyPVVUCKUfpbZlBNcepHMaajg'
usesrid_office='29:1htJmKwuNtPEggpMm5kJ73ht47oIbddUOeEh1r1DFpf7vJmh83_C7Q3sBnFcxS3EJv5hHqcu0Po3_-dMmfqnMfA'
chiahao_usrid='29:1Wp-wm0z5gjBGyNBqmeAnHZVrEz_x8QNh-DQKlIgNuVB59ACaKVJql-cQz2n6IixsodQs12DorLl9c7Rbwi4e9w'
teams_appid='30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
botId='28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
# tenant_id='9255f64b-1818-42e5-ad78-f619a9a7b1e7'
tenant_id='010281b3-d5d6-4bc8-b561-bf4794b97036'

header={'Authorization': 'Bearer ' + access_token} #, 'content-type':'application/json'
url=f'https://smba.trafficmanager.net/apac/v3/conversations'
payload={
    "bot": {
        "id": botId,#30eba4f2-6e15-458b-9fdf-f8bbf25efb4f
        # "name": "AzureBot001_Regis"
    },
    "isGroup": False,
    "members": [
        {
            "id": userId,#usesrid_office,
            "name": "借我測試一下"#"Yi Huang 黃懿"
        }
    ],
    "tenantId": tenant_id,
    "topicName": "Testing proactive msg"
}
response2= requests.post(url,json=(payload), headers=header).content.decode('utf-8')
response2=json.loads(response2)
print('conversationId:\n',response2)
conversation_id=response2["id"]



url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversation_id)
payload={
    "type": "message",
    "from": {
        "id": botId,
        "name": "AzureBot001_Regis"
    },
    "conversation": {
        "id": conversation_id,
        # "name": "test conversation name"
   },
   "recipient": {
        "id":userId,# usesrid_office,
        # "name": "Testing"#"Yi Huang 黃懿"
    },
    "text": "測試測試  我心情好好  祝你也心情很好XDDDDDD",
}

response3 = requests.post(url, json=(payload), headers=header)
response3=response3.content.decode('utf-8')
print('response3',response3)


url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversation_id)
payload={
    "type": "message",
    "from": {
        "id": botId,
        "name": "AzureBot001_Regis"
    },
    "conversation": {
        "id": conversation_id,
        "name": "test conversation name"
   },
   "recipient": {
        "id": userId,
        "name": "Yi Huang 黃懿"
    },
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.hero",
            "content": {
                "title": "title goes here",
                "subtitle": "subtitle goes here",
                "text": "descriptive text goes here",
                "images": [
                    {
                        "url": "https://www.publicdomainpictures.net/pictures/30000/t2/duck-on-a-rock.jpg",
                        "alt": "picture of a duck",
                        "tap": {
                            "type": "playAudio",
                            "value": "url to an audio track of a duck call goes here"
                        }
                    }
                ],
                "buttons": [
                    {
                        "type": "playAudio",
                        "title": "Duck Call",
                        "value": "url to an audio track of a duck call goes here"
                    },
                    {
                        "type": "openUrl",
                        "title": "Watch Video",
                        "image": "https://www.publicdomainpictures.net/pictures/30000/t2/duck-on-a-rock.jpg",
                        "value": "url goes here of the duck in flight"
                    }
                ]
            }
        }
    ]
}

response4 = requests.post(url, json=(payload), headers=header)
response4=response4.content.decode('utf-8')
print('response3',response3)



# cron-messages
# [POST] https://xxxxxx/api/v1/cron-messages

# tenant_id
# {
# 	"user_id": "test",
# 	"employee_id": "test",
# 	"tenant_id": "test"
# }