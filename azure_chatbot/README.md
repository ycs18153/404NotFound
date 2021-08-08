# 用 Azure Bot Framework 實作 Teams Bot 
## 主打功能
* [Link to bot](https://teams.microsoft.com/l/chat/0/0?users=28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f)
點按此連結可以連到teams，開啟此聊天機器人
* 輸入工號連結 teams、line以及 web 服務
    > 工號_XXXXXX
* 輸入help、顯示可以顯示的指令
    > help
* 新增代辦事項，紀錄需要的工作內容
    > 新增代辦事項
* 查看/修改/刪除代辦事項
    > 查看代辦事項
* 輸入 tsmc，連結 my ehr 各項服務
    > my tsmc
* 主動推播訊息提醒代辦事項 (半小時/一小時前各發送一次)

## 建Azure Bot Framework

* [Bot Framework SDK](https://docs.microsoft.com/zh-tw/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
* Azure account_ free for the first year
![](https://i.imgur.com/LJF2tt3.png=200x200)
![](https://i.imgur.com/IIK309n.png=200x200)
* 資源識別碼
```
/subscriptions/82ffd014-405f-4ffa-83d3-e01c0b8c31ce/resourceGroups/azure_bot/providers/Microsoft.BotService/botServices/AzureBotTest001
```
![](https://i.imgur.com/fU8xYEK.png)
* Prequsite
![](https://i.imgur.com/enN30fs.png)
* .env
![](https://i.imgur.com/pciniIm.png)
[管理bot 資源](https://docs.microsoft.com/zh-tw/azure/bot-service/bot-file-basics?view=azure-bot-service-4.0&tabs=csharp)
* az login

![](https://i.imgur.com/q5KautW.png)
```
 "id": "82ffd014-405f-4ffa-83d3-e01c0b8c31ce",
```
```
設定訂用帳戶
az account set --subscription "<azure-subscription-id>"
```
* Azure 應用程式註冊
```
az ad app create --display-name "AzureBot001" --password "ElizaHuangTaigidian2021" --available-to-other-tenants
```
```
得到 (複製並儲存 appId 和 password 值。 在 ARM 部署步驟中，您將需要這些專案。)
{
  "acceptMappedClaims": null,
  "addIns": [],
  "allowGuestsSignIn": null,
  "allowPassthroughUsers": null,
  "appId": "30eba4f2-6e15-458b-9fdf-f8bbf25efb4f",
  "appLogoUrl": null,
  "appPermissions": null,
  "appRoles": [],
  "applicationTemplateId": null,
  "availableToOtherTenants": true,
  "deletionTimestamp": null,
  "displayName": "AzureBot001",
  "errorUrl": null,
  "groupMembershipClaims": null,
  "homepage": null,
  "identifierUris": [],
  "informationalUrls": {
    "marketing": null,
    "privacy": null,
    "support": null,
    "termsOfService": null
  },
  "isDeviceOnlyAuthSupported": null,
  "keyCredentials": [],
  "knownClientApplications": [],
  "logo@odata.mediaContentType": "application/json;odata=minimalmetadata; charset=utf-8",
  "logo@odata.mediaEditLink": "directoryObjects/509ef7da-a9ff-47cc-9670-22b5e700535d/Microsoft.DirectoryServices.Application/logo",
  "logoUrl": null,
  "logoutUrl": null,
  "mainLogo@odata.mediaEditLink": "directoryObjects/509ef7da-a9ff-47cc-9670-22b5e700535d/Microsoft.DirectoryServices.Application/mainLogo",
  "oauth2AllowIdTokenImplicitFlow": true,
  "oauth2AllowImplicitFlow": false,
  "oauth2AllowUrlPathMatching": false,
  "oauth2Permissions": [
    {
      "adminConsentDescription": "Allow the application to access AzureBot001 on behalf of the signed-in user.",
      "adminConsentDisplayName": "Access AzureBot001",
      "id": "eaff0bbf-7f86-4cf3-a697-aecbb02cb813",
      "isEnabled": true,
      "type": "User",
      "userConsentDescription": "Allow the application to access AzureBot001 on your behalf.",
      "userConsentDisplayName": "Access AzureBot001",
      "value": "user_impersonation"
    }
  ],
  "oauth2RequirePostResponse": false,
  "objectId": "509ef7da-a9ff-47cc-9670-22b5e700535d",
  "objectType": "Application",
  "odata.metadata": "https://graph.windows.net/2cb038b5-1b9c-4804-95b1-b4e3642fe824/$metadata#directoryObjects/@Element",
  "odata.type": "Microsoft.DirectoryServices.Application",
  "optionalClaims": null,
  "orgRestrictions": [],
  "parentalControlSettings": {
    "countriesBlockedForMinors": [],
    "legalAgeGroupRule": "Allow"
  },
  "passwordCredentials": [
    {
      "additionalProperties": null,
      "customKeyIdentifier": null,
      "endDate": "2022-07-18T14:31:07.965569+00:00",
      "keyId": "f886311b-4360-413b-b683-eb9afcb06966",
      "startDate": "2021-07-19T14:31:07.965569+00:00",
      "value": null
    }
  ],
  "preAuthorizedApplications": null,
  "publicClient": null,
  "publisherDomain": "eliza85827gmail.onmicrosoft.com",
  "recordConsentConditions": null,
  "replyUrls": [],
  "requiredResourceAccess": [],
  "samlMetadataUrl": null,
  "signInAudience": "AzureADMultipleOrgs",
  "tokenEncryptionKeyId": null,
  "wwwHomepage": null
}
```
* 部署參數
    * deploymentTemplates 中會提供 template-with-new-rg.json 檔案。 這是現有範本檔案的路徑。 其可以是絕對路徑，或目前目錄的相對路徑。 
    * appId-在「建立應用程式註冊」步驟中產生的 JSON 輸出中的 應用程式識別碼 值。
    * appSecret - 您在建立應用程式註冊步驟中提供的密碼。
    * botId -要建立的 Bot 通道註冊資源名稱。 此名稱必須是全域唯一的。 並且會用來作為不可變的 Bot 識別碼。 也可用來作為預設的顯示名稱，而這是可變動的。
    * botSku - 定價層；可以是 F0 (免費) 或 S1 (標準)。
    * newAppServicePlanName - 新應用程式服務方案的名稱。
    * newWebAppName - Bot 應用程式服務的名稱。
    * groupName - 新資源群組的名稱。
    * groupLocation - Azure 資源群組的位置。
    * newAppServicePlanLocation - 應用程式服務方案的位置。
* 現有app service方案建立
```
az deployment group create --resource-group "<name-of-resource-group>" --template-file "<path-to-template-with-preexisting-rg.json>" --parameters appId="<app-id-from-previous-step>" appSecret="<password-from-previous-step>" botId="<id or bot-app-service-name>" newWebAppName="<bot-app-service-name>" existingAppServicePlan="<name-of-app-service-plan>" appServicePlanLocation="<region-location-name>" --name "<bot-app-service-name>"
```

參考：
https://ithelp.ithome.com.tw/articles/10246365

https://docs.microsoft.com/zh-tw/azure/bot-service/bot-builder-deploy-az-cli?view=azure-bot-service-4.0&tabs=python#option-2-new-app-service-plan
> ==[Azure Portal 上的 App registration](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps)==
> 搜尋你剛剛輸入的 displayname，成功的話，就會搜尋的到

![](https://i.imgur.com/n57z5iE.png)
* [將程式碼部署至 Azure](https://docs.microsoft.com/zh-tw/azure/bot-service/bot-builder-deploy-az-cli?view=azure-bot-service-4.0&tabs=python#option-2-new-app-service-plan)
```
az webapp deployment source config-zip --resource-group "azure_bot" --name "AzureBot001" --src "D:\user\AzureBot\echo-bot\echo-bot.zip"
```
> return
```
Getting scm site credentials for zip deployment                                       
Starting zip deployment. This operation can take a while to complete ...              
Deployment endpoint responded with status code 202                                    
{                                                                                     
  "active": true,                                                                     
  "author": "N/A",                                                                    
  "author_email": "N/A",                                                              
  "complete": true,                                                                   
  "deployer": "Push-Deployer",                                                        
  "end_time": "2021-07-19T15:32:00.2950055Z",                                         
  "id": "9681413f17864dbca60570fb10201801",                                           
  "is_readonly": true,                                                                
  "is_temp": false,                                                                   
  "last_success_end_time": "2021-07-19T15:32:00.2950055Z",                            
  "log_url": "https://azurebot001.scm.azurewebsites.net/api/deployments/latest/log",  
  "message": "Created via a push deployment",                                         
  "progress": "",                                                                     
  "received_time": "2021-07-19T15:31:25.6765089Z",                                    
  "site_name": "azurebot001",                                                         
  "start_time": "2021-07-19T15:31:26.9826509Z",                                       
  "status": 4,                                                                        
  "status_text": "",                                                                  
  "url": "https://azurebot001.scm.azurewebsites.net/api/deployments/latest"           
}                                                                                     
```
> second tryout: info returned
```
{
  "active": true,
  "author": "N/A",
  "author_email": "N/A",
  "complete": true,
  "deployer": "Push-Deployer",
  "end_time": "2021-07-19T15:43:03.690509Z",
  "id": "fd9e9f90e7ed478e8c0f56922f1f1beb",
  "is_readonly": true,
  "is_temp": false,
  "last_success_end_time": "2021-07-19T15:43:03.690509Z",
  "log_url": "https://azurebot001.scm.azurewebsites.net/api/deployments/latest/log",
  "message": "Created via a push deployment",
  "progress": "",
  "received_time": "2021-07-19T15:41:54.1387452Z",
  "site_name": "azurebot001",
  "start_time": "2021-07-19T15:41:55.41362Z",
  "status": 4,
  "status_text": "",
  "url": "https://azurebot001.scm.azurewebsites.net/api/deployments/latest"
}
```
* zip 檔要在bot的資料夾下面上傳上去
![](https://i.imgur.com/vCfKHhm.png)
[壓縮示範](https://ithelp.ithome.com.tw/articles/10247572)

* [串到teams](http://studyhost.blogspot.com/2018/07/teamsteams-chat-bot.html?m=1)
從Azure後台的"頻道"，選擇要開啟Azure Bot Framework的平台，例如Teams、Line、Messenger、Outlook等


### 製作 button、實作Hero Card

bot.py 中的 on_message_activity() 修改成以下
```
    async def on_message_activity(self, turn_context: TurnContext):
        print((turn_context.activity))
        # print('activity: ',json.dumps(turn_context.activity, sort_keys=True, indent=4),'\n')
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        if turn_context.activity.text=='todo':
            print('hfeffef')
            contextToReturn=requests.get('https://jsonplaceholder.typicode.com/todos/1').content.decode('utf-8')
        elif turn_context.activity.text=='myehr':
            contextToReturn='https://myehr'
            
        elif turn_context.activity.text=='card':
            def create_hero_card() -> Attachment:
                herocard = HeroCard(title="推薦以下兩個選項", 
                images=[
                    CardImage(
                        url="https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg"
                    )],
                buttons=[
                    CardAction(type=ActionTypes.open_url,title="url1",value="https://www.google.com"),
                    CardAction(type=ActionTypes.open_url,title="url2",value="https://www.yahoo.com"),
                    ])
                return CardFactory.hero_card(herocard)
        
            cardAtt = create_hero_card()
            msg_activity = MessageFactory.attachment(cardAtt)
            await turn_context.send_activity(msg_activity)
        
        else:   
            contextToReturn=f"You said '{ turn_context.activity.text }'"
        if 'contextToReturn' in locals():
            await turn_context.send_activity(contextToReturn)
        print()
```
![](https://i.imgur.com/E1zvsTd.png)


## 亮眼技術
### Adaptive Card
透過包含button、輸入框的Card介面，提供使用者簡易直覺易操作的的環境
![](https://i.imgur.com/0QHJhQ3.png=200x200)
### Sending Proactive Msg(主動推播訊息)

==[**主要依照這篇的步驟**](https://github.com/microsoft/BotFramework-Services/issues/260)==
1. Authorization
> input: appid, app_password
> return: access_token
2. Create conversation
> input: bot_id, user_id, tenantId, access_token in json format
> return: conversation_id
> 
* ["tenantId"須為其中一個屬性](https://stackoverflow.com/questions/48102932/microsoft-teams-bot-could-not-parse-tenant-id)
* [解釋BaseURI，也就是ServiceUrl](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0#create-conversation)
> 那包json應該是其他語言寫法要夾帶的格式，python寫法serviceUrl直接是放在/v3/...前面
> 
> 每個bot的serviceUrl不一樣，要由activity送進來時的turncontext.activity裡面去找

```
        print('turn_context_from_property: \n',turn_context.activity.from_property.as_dict())        
        print('turn_context_conversation: \n',turn_context.activity.conversation.as_dict())
        print('turn_context_recipient: \n',turn_context.activity.recipient.as_dict())
```
> as_dict()方法可以把bot framework 中的物件拆解開成json呈現出來
> 
3. Send msg: 
> input: bot_id, user_id, access_token in json format
> return: response for msg sent

> 將各種訊息在step3 送出，在json中要求的格式
> [Link1](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-send-and-receive-messages?view=azure-bot-service-4.0)
> [Link2](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)
> 中間還有其他的，需要自己點過去看

### Deploy方式

開發時主要在local端起code，透過ngrok給一串外界可以連到的https的網址；deploy bot時用過azure雲端服務、heroku及GCP的App engine，最後決定使用GCP為最終方案。


