import unittest
import LibRestApi
import json
import pickle
import time
import subprocess
class cpaas_pyTest(unittest.TestCase):
    def testscript(self):
        with open("Mobile_TempHumid.txt", "rb") as f2:
            mtemperature = pickle.load(f2)
            mHumidity = pickle.load(f2)
            mstatus = pickle.load(f2)
        print(mtemperature,mHumidity,mstatus)

        endpoint = r'https://a2xjyaic20508y.iot.us-east-1.amazonaws.com/things/Bangalore_Peanut/shadow'
        path = r'/things/Bangalore_Peanut/shadow'

        rest_obj = LibRestApi.REST_API(endpoint,path)
        k = rest_obj.GET()

        d = json.loads(k.text)
        aws_temp = d['state']['desired']['Temperature']
        aws_hum = d['state']['desired']['Humidity']
        aws_swt = d['state']['desired']['Switch']

        print("Temperature =",aws_temp)
        print("Humidity=",aws_hum)
        print("Switch=",aws_swt)

        if int(mtemperature[0:2]) == int(aws_temp):
            print("Temperature value displayed is same on mobile app & AWS cloud")
        else:
            print(" error: Temperature value displayed is not same on mobile app & AWS cloud")
        if int(mHumidity[0:2])== int(aws_hum):
            print("Humidity value displayed is same on mobile app & AWS cloud")
        else:
            print("Error : Humidity value displayed is not same on mobile app & AWS cloud")
        sv = mstatus.split(" ")[2]
        if sv == "OFF" and int(aws_swt)== 2:
            print("HVAC status value displayed is same on mobile app & AWS cloud")
        elif sv == "ON" and int(aws_swt)== 1:
            print("HVAC status value displayed is same on mobile app & AWS cloud")
        else:
            print("Error : HVAC status value displayed is not same on mobile app & AWS cloud")        
            
if __name__ == "__main__":
    unittest.main()
