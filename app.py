from flask import Flask, request
app = Flask(__name__)
import requests
import json
import config
from azure.storage.blob import BlobServiceClient, generate_container_sas, ResourceTypes, AccountSasPermissions, generate_account_sas
from datetime import datetime, timedelta


@app.route("/",  methods = ['GET'])
def home():
    return "Hello, World!"
    
def json_parse(json_object):
    client_id = json_object['client_id']
    client_secret = json_object['client_secret']
    
    return client_id, client_secret

def generate_token():
    blob_service_client = BlobServiceClient(account_url=config.URL, credential=config.SHARED_KEY)
    container_client = blob_service_client.get_container_client("mycontainer")

    # container_token = generate_container_sas(
    #             container_client.account_name,
    #             container_client.container_name,
    #             account_key=container_client.credential.account_key,
    #             policy_id='my-access-policy-id'
    #         )

    sas_token = generate_account_sas(
            blob_service_client.account_name,
            account_key=blob_service_client.credential.account_key,
            resource_types=ResourceTypes(object=True),
            permission=AccountSasPermissions(read=True , write = True, add = True, create = True),
            expiry=datetime.utcnow() + timedelta(hours=1)
        )
    return sas_token

@app.route('/auth', methods = ['POST'])
def get_sas_token():
    import adal
    
    resource = 'https://'+config.STORAGE_ACCOUNT+'.blob.core.windows.net'
    
    application_id ,application_secret = json_parse(request.get_json())

    # get an Azure access token using the adal library
    context = adal.AuthenticationContext(config.AUTHENTICATION_ENDPOINT + config.TENANT_ID)
    token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)

    access_token = token_response.get('accessToken')

    #access_token = auth_check() 
    ## if yes: generate the sas token
    if access_token != '':
        sas_token = generate_token()
        return sas_token
    return 'wrong id or password'

# if __name__ == '__main__':
#     app.run()
