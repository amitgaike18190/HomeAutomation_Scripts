#============================
# @author: Akshatha A S
#============================
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class cpaas_pyTest(unittest.TestCase):
    def setUp(self):
        #binary = FirefoxBinary(r 'C:/Users/akshatha.as/AppData/Local/Mozilla Firefox/firefox.exe')
        #self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver = webdriver.Chrome(r'C:/TestAuto_Setup/chromedriver.exe')
    def tearDown(self):
        print("Done")
        #self.driver.close()
    def testscript(self):
        mydriver=self.driver
        baseurl = "http://52.10.165.197:8080/ProbeOverAirWeb/login.html"
        #username = "Test-Factory_Admin"
        #password = "Accenture@123"
        mydriver.get(baseurl)
        #mydriver.maximize_window()
        time.sleep(2)
        xpaths = { 	
                    'uname' :	'.//*[@name="username"]',
                    'pwd' :	'.//*[@name="userpassword"]',
                    'submit' :	'.//*[text()="Log In"]',
                    'plus' :	'.//*[@id="menuleft"]/div[2]/img[1]',
                    'add_new' :	'.//*[@id="menuleft"]/div[1]/div/div/a[2]',
                    'probe_name' :	'.//*[@id="probe-name"]',
                    'select_device' :	'.//*[@id="selectId1"]',
                    'device_bangalore' :	'.//*[@id="selectId"]/table/tbody/tr[4]/td[1]/input',
                    'script' :	'.//*[@id="trig_file"]',
                    'probe_submit' :	'.//*[@id="submitty"]',
                    'plus' :	'.//*[@id="menuleft"]/div[2]/img[1]',
                    'device_inventory' :    './/*[@id="menuleft"]/div[1]/div/div/a[3]',
                    'banglore_rasp' :	'.//*[text()="PIBANG01"]',
                    'device_status' :	'.//*[text()="Inactive"]',
                    'home'  : './/*[@id="menuleft"]/div[1]/div/div/a[1]',
                    'device' : './/*[@id="menuleft"]/div[1]/div/div/a[3]',
                    'libraries' : './/*[@id="menuleft"]/div[1]/div/div/a[4]',
                    'report' : './/*[@id="menuleft"]/div[1]/div/div/a[5]',
                    'search' : './/*[@id="menuleft"]/div[1]/div/div/a[6]'
                    


                   
                   }
        #Provide Username and password
        print("Login validation")
        mydriver.find_element_by_xpath(xpaths['uname']).send_keys("admin")
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['pwd']).send_keys("admin")
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['submit']).click()
        time.sleep(10)
        print("Successful Login!!!")
        mydriver.find_element_by_xpath(xpaths['plus']).click()
        time.sleep(2)
        #Menu option validation
        print("Validation of Menu options")
        home = mydriver.find_element_by_xpath(xpaths['home']).text
        self.assertEqual(home, "Home", "Home option is not present")
        time.sleep(2)
        add = mydriver.find_element_by_xpath(xpaths['add_new']).text
        self.assertEqual(add, "Add New Test Probes", "Add New Test Probes option is not present")
        time.sleep(2)
        device = mydriver.find_element_by_xpath(xpaths['device']).text
        self.assertEqual(device, "Device Inventory", "Device Inventory option is not present")
        time.sleep(2)
        lib = mydriver.find_element_by_xpath(xpaths['libraries']).text
        self.assertEqual(lib, "Standard Test Libraries", "Standard Test Libraries option is not present")
        time.sleep(2)
        report = mydriver.find_element_by_xpath(xpaths['report']).text
        self.assertEqual(report, "Reports", "Report option is not present")
        time.sleep(2)
        search = mydriver.find_element_by_xpath(xpaths['search']).text
        self.assertEqual(search, "Advanced Search", "Advanced Search option is not present")
        time.sleep(2)
        print("All Menu options are present")
        
        
    
        
if __name__ == "__main__":
    unittest.main()
        
