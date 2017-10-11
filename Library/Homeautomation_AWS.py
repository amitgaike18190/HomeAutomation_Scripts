#============================
# @author: Akshatha A S
#============================
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import re
import pickle
import subprocess

class cpaas_pyTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome('C:\kiran\Chrome\chromedriver.exe')
        #self.driver = webdriver.Chrome(r'C:\Users\akshatha.as\Desktop\Softwares\chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
    def tearDown(self):
        self.driver.close()
        print("Browser closed")
    def testscript(self):
        with open("Mobile_TempHumid.txt", "rb") as f2:
                        mtemperature = pickle.load(f2)
                        mHumidity = pickle.load(f2)
                        mstatus = pickle.load(f2)
        print(mtemperature,mHumidity,mstatus)
        
        mydriver=self.driver
        baseurl = "https://test-factory.signin.aws.amazon.com/console"
        #baseurl = "https://console.aws.amazon.com/iot/home?region=us-east-1#/dashboard"
        #baseurl = "https://us-east-1.signin.aws.amazon.com/console"
        #username = "Test-Factory_Admin"
        #password = "Accenture@123"
        mydriver.get(baseurl)
        #mydriver.maximize_window()
        time.sleep(10)
        xpaths = { 'username' : ".//*[@id='username']",
                   'password' : ".//*[@id='password']",
                   'signin' : ".//*[@id='signin_button']",
                   'aws' : "//*[@class='service' and @href='https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2']",
                   'awsiot' : ".//*[@id='all-services-itemiot']/a/span",
                   'old' : ".//*[@id='c']/div/iot-head-banner/div/button[1]",
                   'search' : ".//*[@ng-model='vm.searchText']",
                   'voltage' : ".//*[@href='#/thing/switch']",
                   'switch' : ".//*[@href='#/thing/Bangalore_Peanut']",
                   'json' : ".//*[@id='state-view']/div[2]/div", 
                   'topic' : ".//*[text()='$aws/things/Voltage/shadow/update']",
                   'client' : ".//*[text()='MQTT Client']",
                   'client_id' : ".//*[@name='clientId']",
                   'connect' : ".//*[@data-type='connectBtnOnclick']",
                   'toast_msg' : ".//*[@id='toast-container']/div",
                   'subscribe' : ".//*[text()='Subscribe to topic']",
                   'sub_topic' : ".//*[@name='subTopicFilter']",
                   'qos' : ".//*[@data-type='subQos1']",
                   'submit' : ".//*[text()='Subscribe']",
                   'fst_value' : "(.//*[@class='ace_constant ace_numeric'])[1] "
                   
                   }
        #time.sleep(20)
        #mydriver.find_element_by_xpath()
        #Provide Username and password
        mydriver.find_element_by_xpath(xpaths['username']).clear()
        mydriver.find_element_by_xpath(xpaths['username']).send_keys("s.reddy.mettukuru")
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['password']).send_keys("Apr@2017")
        time.sleep(5)
        mydriver.find_element_by_xpath(xpaths['signin']).click()
        time.sleep(15)
        #Select AWS_IOT
        mydriver.find_element_by_xpath(xpaths['awsiot']).click()
        time.sleep(15)
        #Find the Voltage
        mydriver.find_element_by_xpath(xpaths['old']).click()
        time.sleep(25)
        #mydriver.find_element_by_xpath(xpaths['voltage']).isDisplyed()
        mydriver.find_element_by_xpath(xpaths['search']).click()
        time.sleep(2)
        #mydriver.find_element_by_xpath(xpaths['search']).clear()
        #time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['search']).send_keys('Bangalore_Peanut')
        time.sleep(25)
        mydriver.find_element_by_xpath(xpaths['switch']).click()
        time.sleep(25)
        JSON = mydriver.find_element_by_xpath(xpaths['json']).text
        #print(JSON)
        #tem = JSON[:20]
        #print("hiiiiiiiiiiiiiii")
        val_dict = JSON[20:100]
        #print("json :")
        #print(val_dict)
        swt =(val_dict.split(",")[0])
        swt1 = swt.split(":")[1]
        print("temperature at AWS cloud:"+swt1[2:4])
        hum = (val_dict.split(",")[1]).split(":")[1]        
        switch = (val_dict.split(",")[2]).split(":")[1]
        print("humidity at AWS cloud :"+hum[2:4])
        #print("HVAC status on cloud:"+switch[0:2])
        switch1 = (str(switch).strip())[0:2]
        print(" HVAC status on AWS cloud:",switch1)
        #print("mHumidity :"+mHumidity)
        #print(swt1[2:4])
        #print(swt1,temp,hum)
        if int(mtemperature[0:2]) == int(swt1[2:4]):
            print("Temperature value displayed is same on mobile app & AWS cloud")
        else:
            print(" error: Temperature value displayed is not same on mobile app & AWS cloud")
        if int(mHumidity[0:2])== int(hum[2:4]):
            print("Humidity value displayed is same on mobile app & AWS cloud")
        else:
            print("Error : Humidity value displayed is not same on mobile app & AWS cloud")
        sv = mstatus.split(" ")[2]
        if sv == "OFF" and int(switch1)== 2:
            print("HVAC status value displayed is same on mobile app & AWS cloud")
        elif sv == "ON" and int(switch1)== 1:
            print("HVAC status value displayed is same on mobile app & AWS cloud")
        else:
            print("Error : HVAC status value displayed is not same on mobile app & AWS cloud")        
            
        #v = dict(val_dict)
        #print(type(v))
        #mydriver.execute_script("window.scrollTo(0, Y)")
        time.sleep(2)
        file1 = r"/home/pi/Desktop/New/AWS/write_to_pi.py"
        sshitem = "python "+file1+" "+mtemperature[0:2]+" "+mHumidity[0:2]+" "+switch1
        abc = [r"C:\Users\deepthi.a.desai\Desktop\Backup\EclipseMars\Putty\PLINK.EXE", "-ssh", "pi@192.168.1.245", "-pw", "raspberry"]
        ss = subprocess.Popen(abc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        time.sleep(4)
        ss.stdin.write(bytes(sshitem + "\n", "ascii"))
        time.sleep(4)
        ss.stdin.flush()
        time.sleep(4)
        ss.stdin.write(bytes("\nexit\n", "ascii"))
        (output, err) = ss.communicate()
        #print("output=", output)
        #print("err=", err) 
        
        
        
if __name__ == "__main__":
    unittest.main()
        
