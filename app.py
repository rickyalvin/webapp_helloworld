from flask import Flask
app = Flask(__name__)
import requests
import json

@app.route("/",  methods = ['GET'])
def home():
    return "Hello, World!"


# def auth_check():
#     url = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F'
#     headers = {'Metadata' : true}
#     r = requests.get(url, headers=headers)
#     response = json.loads(r.content)
#     return response['access_token']
    
    

# @app.route('/auth', methods = ['POST'])
# def get_sas_token():
    
#     access_token = auth_check()
#     if access_token != '':
#         return 'it worked!'
#     return 'failed'


if __name__ == '__main__':
    app.run()
