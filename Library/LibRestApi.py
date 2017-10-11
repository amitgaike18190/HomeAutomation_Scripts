#---------------------------------------------------------------------------#
# Authour: Shilpa                                                           #
# Description : Program to execute post and get methods of REST API         #
# Date :08-08-2017                                                          #
#---------------------------------------------------------------------------#

#************************ General Python imports ****************************#
import sys
import os
import json
import base64
import datetime
import hashlib
import hmac
import requests
import pickle

#************************ Main **********************************************#
class REST_API:
    def __init__(self,endpoint,path):
        '''
        setting variable values
        '''
        try:
            output = open("credential", "rb")
            credential = pickle.load(output)
            output.close()
        except FileNotFoundError:
            print("credential file not found")

        self.access_key = credential['access_key']
        self.secret_key = credential['secret_key']
        self.service = 'iotdata'
        self.host = credential['host']
        self.region = 'us-east-1'
        self.endpoint = endpoint
        self.path = path
        if self.access_key is None or self.secret_key is None:
            print('No access key is available.')
            sys.exit()
        else:
            pass


    def sign(self,key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def getSignatureKey(self,key, date_stamp, regionName, serviceName):
        """
        Description:-     Method to get awsSignature Key

        """

        kDate = self.sign(('AWS4' + key).encode('utf-8'), date_stamp)
        kRegion = self.sign(kDate, regionName)
        kService = self.sign(kRegion, serviceName)
        kSigning = self.sign(kService, 'aws4_request')
        return kSigning

    def awsSignature(self,method,content_type,request_parameters=None):
        """
        Description:-     Method to get awsSignature

        """
        t = datetime.datetime.utcnow()
        amz_date = t.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = t.strftime('%Y%m%d')
        #canonical_uri = self.path
        canonical_querystring = ''
        canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + self.host + '\n' + 'x-amz-date:' + amz_date + '\n'
        signed_headers = 'content-type;host;x-amz-date'
        payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()
        canonical_request = method + '\n' + self.path + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
        #print(canonical_request)

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = date_stamp + '/' + self.region + '/' + self.service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(
            canonical_request.encode('utf-8')).hexdigest()
        #print(string_to_sign)
        # Create the signing key using the function defined above.
        signing_key = self.getSignatureKey(self.secret_key, date_stamp, self.region, self.service)

        # Sign the string_to_sign using the signing_key
        signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
        # Put the signature information in a header named Authorization.
        authorization_header = algorithm.strip() + ' ' + 'Credential=' + self.access_key.strip() + '/' + credential_scope.strip() + ', ' + 'SignedHeaders=' + signed_headers.strip() + ', ' + 'Signature=' + signature.strip()
        #print("credential_scope==========", credential_scope)
        headers = {'Content-Type': content_type,
                   'Host': self.host,
                   'X-Amz-Date': amz_date,
                   'Authorization': authorization_header}
        return headers

    def GET(self,content_type = 'application/x-www-form-urlencoded'):
        """
            Authour:-         Shilpa
            Description:-     Method to call REST API's GET method
            Input Paramters:- content_type
            Return:-          response
        """
        headers = self.awsSignature("GET",content_type,'')
        response = requests.request("GET", self.endpoint, headers=headers)
        print(response.text)
        return response

    def POST(self,post_data,content_type = 'application/json'):
        """
            Authour:-         Shilpa
            Description:-     Method to call REST API's POST method to post data
            Input Paramters:- data to be posted, content_type
            Return:-          response
        """
        headers = self.awsSignature("POST",content_type,request_parameters=post_data)
        request_parameters = post_data
        response = requests.post(url=self.endpoint, data=request_parameters, headers=headers)
        print(response.text)
        return response


if __name__ == '__main__':
    endpoint = r'https://a2xjyaic20508y.iot.us-east-1.amazonaws.com/things/Bangalore_Peanut/shadow'
    path = r'/things/Bangalore_Peanut/shadow'
    #endpoint = r'https://a2xjyaic20508y.iot.us-east-1.amazonaws.com/things/output_switch1_blr/shadow'
    #path = r'/things/output_switch1_blr/shadow'
    rest_obj = REST_API(endpoint,path)
    #rest_obj.GET()
    '''
    post_data = '{ \
     "state":{\
      "desired": {\
        "switch_status": "00",\
    "temp": "39",\
    "humidity": "90"\
      } }\
     }'
	 '''
    #rest_obj.POST(post_data)
    k = rest_obj.GET()
    #print("k=", type(k.text), k.text)
    d = json.loads(k.text)
    print("d",d['state']['desired']['Temperature'])
    print(d['state']['desired']['Humidity'],d['state']['desired']['Switch'])

#ok = output_switch.get_switch_value()
#print("ok",ok[2])
"""
post_data = '{ \
 "state":{\
  "desired": {\
    "switch_val":ok[2] \
  } }\
}'
"""
#rest_obj.POST(post_data,content_type = 'application/json')
#ok = output_switch.set_switch_value()'''
