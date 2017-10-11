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
import fileinput
import autoit
from datetime import datetime
import time
import getpass
import subprocess


class cpaas_pyTest(unittest.TestCase):
    def setUp(self):
        #binary = FirefoxBinary('C:/Users/akshatha.as/AppData/Local/Mozilla Firefox/firefox.exe')
        #self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver = webdriver.Chrome(r'chromedriver.exe')
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
                    #'Home' : './/*[text()="Home"]',
                    'Home' : './/*[@class="btn btn-success btn-lg"]',
                    #'h' : './/*[@href="device_avail.html"]',
                    'search_probe' : './/*[@placeholder="Search by Probe Name"]',
                    #'details' : './/*[text()="Details"]',
                    'details' : './/*[@ng-click="fun(dashboard)"]',
                    'report' : '//body/div[3]/div[3]/div[2]/table/tbody/tr/td[3]',
                    'reportdownlod' : './/*[text()="Report"]'
                    


                   
                   }
        date =  str(datetime.now())
        print(date)
        d=date.replace(':','')
        e=d.replace('.','')
        f=e.replace('-','')
        g=f.replace(' ','')
        print(g)
        #Provide Username and password
        mydriver.find_element_by_xpath(xpaths['uname']).send_keys("admin")
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['pwd']).send_keys("admin")
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['submit']).click()
        time.sleep(10)
        #Select AWS_IOT
        mydriver.find_element_by_xpath(xpaths['plus']).click()
        time.sleep(10)
        #Find the Voltage
        #mydriver.find_element_by_xpath(xpaths['voltage']).isDisplyed()
        mydriver.find_element_by_xpath(xpaths['add_new']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['probe_name']).send_keys("T"+g)
        mydriver.find_element_by_xpath(xpaths['probe_name']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['select_device']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['device_bangalore']).click()
        mydriver.find_element_by_xpath(xpaths['probe_name']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['script']).click()
        autoit.win_wait_active("Open", 10)
        path = r"TempHumid.py"
        print(path)
        time.sleep(2)
        #autoit.send(os.path.join(path))
        autoit.send(path)
        autoit.send("{ENTER}")
        mydriver.find_element_by_xpath(xpaths['probe_submit']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['Home']).click()
        time.sleep(2)
        mydriver.find_element_by_xpath(xpaths['search_probe']).send_keys("T"+g)
        time.sleep(4)
        mydriver.find_element_by_xpath(xpaths['details']).click()
        time.sleep(2)
        rep = mydriver.find_element_by_xpath(xpaths['report']).text
        print(rep)
        time.sleep(2)
        count = 0
        while True:
            if(rep == 'Completed'):
                #Download Report reportdownlod
                mydriver.find_element_by_xpath(xpaths['reportdownlod']).click()
                print("Report is downloaded...")
                time.sleep(2)
                break
            count= count+1
            time.sleep(2)
            if count ==3:
                print("Probe execution is pending")
                break
        print("Done")
        #REPORT VALIDATION
        time.sleep(10)
        user = getpass.getuser()

        path = r"C:\Users\%s\Downloads\downloadname.txt"%user
        print(path)


        with open(path,"r") as f:
            for line in f:
                print(line)
                hum,temp = line.split(" ")[0],line.split(" ")[1]
                break
                

        print("hum,temp",hum,temp)

        file1 = r"/home/pi/Desktop/POTA/DeviceTempHumidComp.py"
        sshitem = "sudo python "+" "+file1+" "+hum+" "+temp
        abc = [r"C:\Program Files (x86)\PuTTY\plink.exe", "-ssh", "pi@192.168.0.5", "-pw", "raspberry"]
        ss = subprocess.Popen(abc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        time.sleep(4)
        ss.stdin.write(bytes(sshitem + "\n", "ascii"))
        time.sleep(4)
        ss.stdin.flush()
        time.sleep(4)
        ss.stdin.write(bytes("\nexit\n", "ascii"))
        (output, err) = ss.communicate()
        print("output=", output)
        print("err=", err) 
        
if __name__ == "__main__":
    unittest.main()
        
