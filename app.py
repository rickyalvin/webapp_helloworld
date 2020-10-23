from flask import Flask, request
app = Flask(__name__)
import requests
# import json

@app.route("/",  methods = ['GET'])
def home():
    return "Hello, World!"
    
def json_parse(request):
	req_data = request.get_json()
	client_id = req_data['client_id']
	client_secret = req_data['client_secret']
    
    return client_id, client_secret

@app.route('/auth', methods = ['POST'])
def get_sas_token():
    import adal

    authentication_endpoint = 'https://login.microsoftonline.com/'
    resource  = 'https://management.core.windows.net/'
    storage_account = 'storagetestcz'
    tenant_id = '24041256-c834-468a-b7e7-c4dc34322cfe'
    
    resource = 'https://'+storage_account+'.blob.core.windows.net'
    
    application_id ,application_secret = json_parse(request)

    # get an Azure access token using the adal library
    context = adal.AuthenticationContext(authentication_endpoint + tenant_id)
    token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)

    access_token = token_response.get('accessToken')

    #access_token = auth_check()
    if access_token != '':
        return 'it worked!'
    return 'failed'
