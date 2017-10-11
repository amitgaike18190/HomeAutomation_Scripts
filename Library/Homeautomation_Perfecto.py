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
#from appium import webdriver
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
#from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
#from RemoteWebDriverUtils import RemoteWebDriverUtils

class AndroidTests(unittest.TestCase):
    def setUp(self):
        
        #=============== HOAMEAUTOMATION APP ====================================================== 
        #Perfecto driver creation
        # Create a desired capabilities object as a starting point.
        capabilities = {'browserName': 'mobileOS', 'version':'', 'platform':'ANY'}
        
        # authentication information for connection to the MobileCloud
        host = 'accenture.perfectomobile.com'
        capabilities['user'] = 'akshatha.as@accenture.com'
        capabilities['password'] = 'akshatha1234'
        
        # To run this script against certain device
        # Specify that device's ID below
        capabilities['deviceName'] = '194D312D'
        capabilities['appPackage'] = 'iot.accenture.com.iotapplication'
        
        # Use device opened in MobileCloud Recording window
        #RemoteWebDriverUtils.set_execution_id_capability(capabilities)
        capabilities['automationName'] = 'PerfectoMobile'
        
        # Create driver with call to RWD Url
        self.device1 = webdriver.Remote("https://" + host + "/nexperience/perfectomobile/wd/hub", capabilities)
        

    def tearDown(self):
        "Close Application"
        self.device1.quit()
        
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
        w =WebDriverWait(self.device1, 50) # Appium web deriver
        #element = w.until(EC.presence_of_element_located((By.ID,Beakon['temperature'])))
        #self.device1.find_element_by_xpath(Beakon['Menu']).click()
        time.sleep(10)
        print('Execution started!!')
        time.sleep(10)
        self.device1.find_element_by_id(Beakon['settings']).click()
        self.device1.find_element_by_id(Beakon['threshold']).clear()
        self.device1.find_element_by_id(Beakon['threshold']).send_keys(threshold)
        self.device1.find_element_by_id(Beakon['time']).clear()
        self.device1.find_element_by_id(Beakon['time']).send_keys(t)
        self.device1.find_element_by_id(Beakon['save']).click()
        # Check the heater control status
        self.device1.back()
        time.sleep(2)
        self.device1.back()
        # get the actual temperature
        temperature = self.device1.find_element_by_id(Beakon['temperature']).text
        Humidity = self.device1.find_element_by_id(Beakon['humidity']).text
        print("Actual temperature :" +temperature)
        print("Threshold temperature : "+str(threshold))
        
        status = self.device1.find_element_by_id(Beakon['heating']).text
        print("Heating control status :"+status)
        time.sleep(4)
        file1 = open("Mobile_TempHumid.txt", "wb")
        pickle.dump(temperature, file1)
        pickle.dump(Humidity, file1)
        pickle.dump(status, file1)
        file1.close()
        
        
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
