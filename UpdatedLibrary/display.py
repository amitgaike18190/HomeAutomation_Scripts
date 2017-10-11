#-----------------------------------------------------------------------------------#
# Authour: Shilpa                                                                   #
# Description : Program to write log to test-report.js file and discplay the output #
# Date :09-01-2017                                                                  #
#-----------------------------------------------------------------------------------#

#************************ General Python imports ***************************#
import os
import time
#import webbrowser
#************************ Local imports ************************************#
#
#************************ Main *********************************************#
gcount = 0
pcount = 0
fcount = 0
total = 0
skipcount = 0
current = os.getcwd()
test_report_js = os.path.join(r'',current,'js','test-report.js')
#**************************** update_jsfile() *************************************#
def update_jsfile(cmd, count,step, cmd_type, cmd_dict_1, cmd_status_1,svalue,session_name=1):
        '''
        Authour:-         Shilpa
        Description:-     Method to write result(log) of each command to test-report.js file
        Input Paramters:- Sesson name, command name, count of commands, output, status-passed/failed
        Return:-          None
        '''

        #print("he",cmd, count,step, cmd_type, cmd_dict_1, cmd_status_1,svalue)
        global pcount
        global fcount
        global total
        global skipcount
        global gcount
        gcount = gcount + 1
        num = gcount

        valueJsChange = """{
          "testCaseName" : "%s",
          "steps" : [ {
            "no" : %d,
            "testClassName" : " %s ",
            "name" : " %s ",
            "status" : 1,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551656538,
            "stackTrace" :  "%s" ,
            "exceptionMessage" : "Test Logs",
            "screenShots" : [ ],
            "statusValue" : " %s ",
            "statusIcon" : "%s",
            "session" : " %s "
          } ]
        },"""%(cmd, num,step,cmd_type,(((str(cmd_dict_1).strip('[]')).replace('"',''))).replace('\\',''), cmd_status_1,svalue,session_name)

        with open(test_report_js, "a+") as newJSFile:
            newJSFile.write(valueJsChange)

        if (cmd_status_1 == "Failed"):
            fcount = fcount + 1
        elif (cmd_status_1 == "Passed"):
            pcount = pcount + 1
        else:
            skipcount = skipcount + 1
        total = total + 1



#**************************** initial_update() *************************************#
def initial_update():
        '''
        Authour:-         Shilpa
        Description:-     Method to update first part of test-report.js file
        Input Paramters:- None
        Return:-          None
        '''
        formatJS = """
            var result = {
              "scenarios" : [ {
                  "scenarioName" : "",
                  "testCases" : ["""
        with open(test_report_js, "w+") as newJSFile:
            newJSFile.write(formatJS)


#**************************** final_update() *************************************#
def final_update():
        '''
        Authour:-         Shilpa
        Description:-     Method to update last part of test-report.js file
        Input Paramters:- None
        Return:-          None
        '''
        global total
        global pcount
        global fcount
        formatJS1 = """
            ],
            "nativeReports" : [ ],
            "metrics" : {
              "total" : %d,
              "passed" : %d,
              "failed" : %d,
              "skipped" : 0,
              "startTimeInMillis" : 1465551628147,
              "endTimeInMillis" : 1465551886340
             
            }
          } ],
          "metrics" : {
            "total" : %d,
            "passed" : %d,
            "failed" : %d,
            "skipped" : 0,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551886340
           
          }
        }

            """ % (total, pcount, fcount, total, pcount, fcount)
        # time.sleep(100)
        with open(test_report_js, "ba+") as newJSFile:
            newJSFile.seek(-1, 1)
            newJSFile.truncate()
            newJSFile.write(formatJS1.encode("ascii"))
        time.sleep(10)
        #webbrowser.open(r"file://C:/Project work/Feb 13/Run33.2/index.html")
