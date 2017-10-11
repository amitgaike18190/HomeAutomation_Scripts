#-----------------------------------------
#-------@Author: AKSHATHA A S-------------
#-----------------------------------------
import openpyxl
import re
import os
import os.path
import sys
import subprocess
import time
import unittest
from appium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import requests
import json
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pickle
class AndroidTests(unittest.TestCase):
    def setUp(self):
        
        #=============== HOAMEAUTOMATION APP ====================================================== 
        print("\n----Installing the Application on mobile device----")
        desired_caps1 = {}
        desired_caps1['platformName'] = 'Android'
        desired_caps1['platformVersion'] = '7.0'
        desired_caps1['deviceName'] = 'ZY223BKGT7'#'461bd0ba'#ZY223BKGT7
        #desired_caps1['deviceName'] = '192.168.0.3:5555'
        desired_caps1['appPackage'] = 'iot.accenture.com.iotapplication'
        desired_caps1['app'] = r"C:\Users\deepthi.a.desai\.jenkins\jobs\ConnectedHome_Scan\workspace\HomeAutomationUseCase\app\build\outputs\apk\app-debug.apk"
        
        #desired_caps1['appPackage'] = 'iot.accenture.com.beakonsimulator'
        #desired_caps1['appActivity'] = '.MainActivity'
        desired_caps1['appActivity'] = 'com.iot.fragments.ControlPanelActivity'
        self.device1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)
        print("Home Automation App is launched")

    def tearDown(self):
        "Close Application"
        #self.device1.quit()
        
    def test_andapp(self):
        threshold = 20
        t = 1
        Beakon = { 'Menu' : "//android.widget.ImageView[@content-desc='More options']",
               'settings' : 'iot.accenture.com.iotapplication:id/settingView',
               'threshold' : 'iot.accenture.com.iotapplication:id/thresholdValue',
                'time' : 'iot.accenture.com.iotapplication:id/timerValueEditText',
                'save':'iot.accenture.com.iotapplication:id/savebutton',
                'heating': 'iot.accenture.com.iotapplication:id/heating_control',
                'heatinh_switch' : '//android.widget.Switch[@index=1]',
                'temperature' : 'iot.accenture.com.iotapplication:id/TemperatureBtn',
                'humidity' : 'iot.accenture.com.iotapplication:id/HumidityBtn'
                   
            }
        #Wait till the page loads
        #time.sleep(5)
        #w =WebDriverWait(self.device1, 20) # Appium web deriver
        #element = w.until(EC.presence_of_element_located((By.ID,Beakon['temperature'])))

        while(True):
            temperature = self.device1.find_element_by_id(Beakon['temperature']).text
            if(temperature != "..."):
                print(temperature)
                break
            
        
        self.device1.find_element_by_id(Beakon['settings']).click()
        self.device1.find_element_by_id(Beakon['threshold']).clear()
        self.device1.find_element_by_id(Beakon['threshold']).send_keys(threshold)
        #self.device1.find_element_by_id(Beakon['time']).clear()
        #self.device1.find_element_by_id(Beakon['time']).send_keys(t)
        self.device1.find_element_by_id(Beakon['save']).click()
        # Check the heater control status
        self.device1.back()
        time.sleep(2)
        self.device1.back()
        
        # get the actual temperature
        temperature = self.device1.find_element_by_id(Beakon['temperature']).text
        Humidity = self.device1.find_element_by_id(Beakon['humidity']).text
        status = self.device1.find_element_by_id(Beakon['heating']).text
        
        print("Threshold temperature set on mobile application : "+str(threshold))
        print("Temperature value displayed on mobile application :" +temperature)
        print("Humidity value displayed on mobile application :" +Humidity)
        print("HVAC status on mobile application:"+status)
        
        time.sleep(2)
        file1 = open("Mobile_TempHumid.txt", "wb")
        pickle.dump(temperature, file1)
        pickle.dump(Humidity, file1)
        pickle.dump(status, file1)
        file1.close()
        
        
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
