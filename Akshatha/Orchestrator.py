#---------------------------------------------------------------------------#
# Authour: Nishant, Shilpa                                                  #
# Description : Program to execute commands and get output for each command #
# Date :09-01-2017                                                          #
#---------------------------------------------------------------------------#

#************************ General Python imports ***************************#
import re
import json
import os
import sys
import time
import subprocess
import threading
import logging
import webbrowser
from multiprocessing import Process, Lock
#************************ Local imports ************************************#
#import myxml_
import UniqueSessions
import reporting
import display as d
#************************ Main *********************************************#

current = os.getcwd()
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s %(asctime)s ')
html_path = os.path.join(r'file://',current,'index.html')
#**************************** execution() *************************************#

def execution():
    '''
    Authour:-     Nishant, Shilpa
    Description:- calls the methods open_cmd(), open_ssh()depending on the type(cmd/ssh) command
                  and also writes to .js file. Finally opens index.html file in default web browser.
    Input Paramters:- None
    Return:-          None
    '''
    cmd_path = sys.argv[1]
    r = reporting.Report()
    d.initial_update()
    cmd_th = []
    ssh_th = []

    try:
        row, name, lists, cmd_name=UniqueSessions.session(cmd_path)
        #print(" #######################",cmd_name)
        for item in lists:
            print(item)
        #print(lists)
        count=0  
        for se in name:
            #print("*********************",cmd_name[count])
            logging.debug("Session: %s  \n Command to be executed: %s",se,lists[count])
            #print(count)
            if cmd_name[count]=="cmd":
                print(lists[count])
                th = threading.Thread(name=se,target=r.open_cmd, args=(se,lists[count]))
                th.start()
                time.sleep(10)
                cmd_th.append(th)
                count=count+1
            else:
                pass
            if cmd_name[count]=="ssh":
            	th = threading.Thread(name=se,target=r.open_ssh, args=(se,lists[count]))
            	th.start()
            	time.sleep(10)
            	ssh_th.append(th)
            else:
                pass

            #count=count+1
            print(count)
    except Exception as e:
        logging.debug(e)
    for ths in cmd_th:
        ths.join()
		
    for ths in ssh_th:
        ths.join()

    d.final_update()
    time.sleep(10)
    webbrowser.open(html_path)
    
    

        
if __name__=='__main__':
    execution()


