from fyers_api import accessToken
from fyers_api import fyersModel
import webbrowser
import hashlib


redirect_uri= "https://www.google.com/"  ## redircet_uri you entered while creating APP.
client_id = "LB65IDSEJH-100"                                          ## Client_id here refers to APP_ID of the created app
secret_key = "22POK2EVJ2"                                           ## app_secret key which you got after creating the app 
grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
response_type = "code"                             ## The response_type always has to be "code"
state = "OK"   


appSession = accessToken.SessionModel(client_id = client_id, redirect_uri = redirect_uri,response_type=response_type,state=state,secret_key=secret_key,grant_type=grant_type)

### Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code 
generateTokenUrl = appSession.generate_authcode()

print((generateTokenUrl))  
webbrowser.open(generateTokenUrl,new=1)


auth_code = input("Please enter something: ")
appSession.set_token(auth_code)
response = appSession.generate_token()

### There can be two cases over here you can successfully get the acccessToken over the request or you might get some error over here. so to avoid that have this in try except block
try: 
    access_token = response["access_token"]
except Exception as e:
    print(e,response) 
print(access_token)