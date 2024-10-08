import requests
from flask import Flask,jsonify
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

app = Flask(__name__)

api_key = 'secret'
client = CfClient(api_key)
client.wait_for_initialization()

beta_testers = Target(identifier="test1", name="test1", attributes={"org": "blue"})

HOST_NAME= 'http://flask-service:8989'
SERVICE_PATH= '/getproductdetails'

URL= HOST_NAME+SERVICE_PATH


def validate(response):

    if "P" in response:
        return True
    else:
        return False

@app.route('/')
def hello():
  return 'Welcome to the Site'

def get_flag_status(flagstate):
    return client.bool_variation(flagstate, beta_testers, False)


@app.route('/productdetails', methods=['GET'])
def product_details():
    result = get_flag_status("ProductDetails")
    
    if result:

        response = requests.get(URL)
        response = str(response.content)
    
        print('My response is :',response)

        if(validate(response)):
            return jsonify(response)

        else:
            return "Bad Request, Corrupted Response", 500
        
    else:
        return jsonify({"error": "Feature Not Available"}), 404



if __name__ == '__main__':

    app.run(debug=True)
