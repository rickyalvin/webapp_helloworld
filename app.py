from flask import Flask
app = Flask(__name__)
import requests
# import json

@app.route("/",  methods = ['GET'])
def home():
    return "Hello, World!"


# def auth_check():
#     url = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F'
#     headers = {'Metadata' : true}
#     r = requests.get(url, headers=headers)
#     response = json.loads(r.content)
#     return response['access_token']
    
    

@app.route('/auth', methods = ['POST'])
def get_sas_token():
    import adal

    tenant_id = '24041256-c834-468a-b7e7-c4dc34322cfe'

    resource = 'https://storagetestcz.blob.core.windows.net'

    application_id = 'acb4395e-5f21-4001-9a9d-bc83664fedbc'
    application_secret = 'CNjT8dMmVReuDHK.SVea11XIp-~aPr_60F'
    authentication_endpoint = 'https://login.microsoftonline.com/'
    resource  = 'https://management.core.windows.net/'

# get an Azure access token using the adal library
    context = adal.AuthenticationContext(authentication_endpoint + tenant_id)
    token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)

    access_token = token_response.get('accessToken')
    print(access_token)

#     access_token = auth_check()
    if access_token != '':
        return 'it worked!'
    return 'failed'



# app.run()
