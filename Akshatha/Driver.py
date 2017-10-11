'''
Created on Jan 17, 2017

@author: deepthi.a.desai
'''
from selenium import webdriver  
def Initialize():
    global driver
    desired_caps = {}
    #Android Native applications
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'ZY223NZ42R' 
    #desired_caps['appPackage'] = 'iot.accenture.com.beakonsimulator'
    #desired_caps['appActivity'] = 'iot.accenture.com.beakonsimulator.MainActivity'
    desired_caps['app'] = r'C:\Users\shilpa.alagundi\Documents\deepti\WareHouse.apk'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 
    return driver
def CloseDriver():
    driver.close()
    driver.quit()
def context_switch():
    current = driver.current_context
    driver.contexts
    context_name = "WEBVIEW_1"
    driver.switch_to.context(context_name)

    
    
    
