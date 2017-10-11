#-----------------------------------------------------------------------------#
# Authour: Shilpa                                                             #
# Description : Program to execute commands and capture logs                  #
# Date :01-02-2017                                                            #
#-----------------------------------------------------------------------------#

#************************ General Python imports ****************************#
import unittest
import webbrowser
import time
import subprocess
import threading
import logging
import os
#from selenium import webdriver
#************************ Local imports *************************************#
import display
#************************ Main **********************************************#

cmd_dict= dict()
ssh_dict =dict()
sel_dict = dict()
app_dict = dict()
cmd_count = 0

class Report(unittest.TestCase):
    #**************************** seleniumReport() *************************************#
    def seleniumReport(self, test_name, assert_type, step_name=None, actual_value=None, expected_value=None, pass_message=None, fail_message=None):
        '''
        Authour:-         Shilpa
        Description:-     Method to capture selenium scripts output logs
        Input Paramters:- test_name, assert_type, step_name, actual_value, expected_value, pass_message, fail_message
        Return:-          None
        '''
        self.test_name = test_name
        self.step_name = step_name
        self.pass_message = pass_message
        self.fail_message = fail_message
        self.condition = actual_value
        self.sel_true = True
        global sel_dict
        if not sel_dict:
            sel_dict[self.test_name] = list()

        if assert_type == "assertEqual":
            try:
                self.assertEqual(actual_value, expected_value, self.fail_message)
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                self.sel_true = False
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.fail_message)
                sel_dict[self.test_name].append(err)

        elif assert_type == "assertTrue":
            try:
                self.assertTrue(self.condition, self.fail_message)
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                self.sel_true = False
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.fail_message)
                sel_dict[self.test_name].append(err)

        elif assert_type == "assertFalse":
            try:
                self.assertFalse(self.condition, self.fail_message)
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                self.sel_true = False
                sel_dict[self.test_name].append(self.step_name)
                sel_dict[self.test_name].append(self.fail_message)
                sel_dict[self.test_name].append(err)

        elif assert_type == "remaining types":
            pass
            #code continues

        else:
            pass

        return self.sel_true

    #**************************** appiumReport()   *************************************#
    def appiumReport(self, test_name, assert_type, step_name=None, actual_value=None, expected_value=None, pass_message=None, fail_message=None):
        '''
        Authour:-         Shilpa
        Description:-     Method to capture appium scripts output logs
        Input Paramters:- test_name, assert_type, step_name, actual_value, expected_value, pass_message, fail_message
        Return:-          None
        '''
        self.test_name = test_name
        self.step_name = step_name
        self.pass_message = pass_message
        self.fail_message = fail_message
        self.condition = actual_value
        global app_dict
        app_dict[test_name] = list()

        if assert_type == "assertEqual":
            try:
                self.assertEqual(actual_value, expected_value, self.fail_message)
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.fail_message)
                app_dict[self.test_name].append(err)
        elif assert_type == "assertTrue":
            try:
                self.assertTrue(self.condition, self.fail_message)
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.fail_message)
                app_dict[self.test_name].append(err)

        elif assert_type == "assertFalse":
            try:
                self.assertFalse(self.condition, self.fail_message)
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.pass_message)
            except AssertionError as err:
                app_dict[self.test_name].append(self.step_name)
                app_dict[self.test_name].append(self.fail_message)
                app_dict[self.test_name].append(err)


        elif assert_type == "remaining types":
            pass
            #code continues

        else:
            pass

        #return self.result
        
    #**************************** get_sel_log() *************************************#
    def get_sel_log(self,test_name):
        '''
        Authour:-         Shilpa
        Description:-     Method to gather selenium scripts output logs
        Input Paramters:- test_name
        Return:-          Complete log of selenium script
        '''
        global sel_dict
        #print(sel_dict[test_name])
        for value in sel_dict[test_name]:
            print(value)
        return sel_dict[test_name]
    
    #**************************** get_app_log() *************************************#
    def get_app_log(self,test_name):
        '''
        Authour:-         Shilpa
        Description:-     Method to gather appium scripts output logs
        Input Paramters:- test_name
        Return:-          Complete log of appium script
        '''
        global app_dict
        #print(app_dict[test_name])
        for value in app_dict[test_name]:
            print(value)

        return app_dict[test_name]
    
    #**************************** capture_log() *************************************#
    def capture_log(self,session_name, cmd, cmdtype):
        '''
        Authour:-         Shilpa
        Description:-     Method to captures result(output/error) of each command
        Input Paramters:- Sesson name, command name,cmdtype = cmd/ssh
        Return:-          result(output/error) and status = Passed/Failed
        '''

        cmd_status = dict()
        cmd_dict = dict()
        cmd_found = False
        E = False
        #errors = False
        if cmdtype == "cmd":
            outfile1 = str(session_name)
            errfile1 = "err_" + str(session_name)
        elif cmdtype == "ssh":
            outfile1 = "sshout_" + str(session_name)
            errfile1 = "ssherr_" + str(session_name)
        cmd_status[cmd] = "Passed"
        outfile = os.path.join(os.getcwd(),"Logs",outfile1)
        errfile = os.path.join(os.getcwd(),"Logs",errfile1)
        with open(outfile, "r+") as f:
            cmd_dict[cmd] = list()
            #cmd_status[cmd] = "Passed"
            with open(errfile, "r+") as f2:
                for line2 in f2.readlines():
                    if cmd in line2 or cmd.split(' ')[1] in line2:
                        print("kk",cmd,line2)
                        E = True
                        cmd_status[cmd] = "Failed"

                    if E:
                        if line2.endswith('\.'):
                            # cmd_dict[cmd].append(line2)
                            break
                        elif (str(line2).find('error') != -1) or (str(line2).find('Error') != -1):
                            cmd_status[cmd] = "Failed"
                            cmd_dict[cmd].append(line2)
                        else:
                            cmd_dict[cmd].append(line2)

            for line in f.readlines():
                if E:
                    break
                elif cmd in line:
                    cmd_found = True
                    cmd_dict[cmd].append(line)
                    continue
                if cmd_found:
                    # print("cmd",cmd)
                    if line.startswith('C:\\') or (str(line).find(';pi@raspberrypi:') != -1) or (str(line).find(';pi@PIBANG01:') != -1):
                        break
                    elif (str(line).find('error') != -1) or (str(line).find('Error') != -1):
                        cmd_status[cmd] = "Failed"
                        cmd_dict[cmd].append(line)
                        #errors = True
                    else:
                        cmd_dict[cmd].append(line)

            print(cmd, "status=", cmd_status[cmd])
        return cmd_status[cmd], cmd_dict[cmd]
    
    #**************************** open_cmd() *************************************#
    def open_cmd(self,session_name, descr):
        '''
        Authour:-         Shilpa
        Description:-     Method to execute list of commands of type 'cmd' of a given session
        Input Paramters:- Sesson name, list of commands to be executed
        Return:-          None
        '''
        try:
            print("session here----------", session_name)
            logging.debug('Active threads are: %s', threading.enumerate())
            # s=session_name
            if os.path.exists(os.path.join(os.getcwd(),"Logs")):
                pass
            else:
                os.mkdir("Logs")
            

            s = subprocess.Popen("cmd /K ", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for item in descr:
                print("my",item)

                s.stdin.write(bytes(item + "\n", "ascii"))
                s.stdin.flush()
                logging.debug("Completing Command execution: %s", item)
            (output, err) = s.communicate()
            print("output=",output)
            print("err=",err)

            outfile1 = str(session_name)
            errfile1 = "err_" + str(session_name)

            outfile = os.path.join(os.getcwd(),"Logs",outfile1)
            errfile = os.path.join(os.getcwd(),"Logs",errfile1)
            with open(errfile, "w+") as f:
                f.write(err.decode('utf-8'))
            with open(outfile, "w+") as f:
                print("writing to file")
                if b"\xb0" in output:
                    output = output.replace(b'\xb0C',b' Degree Celsius')
                f.write(output.decode('utf-8'))

            cmd_status = dict()
            cmdtype = "cmd"
            for cmd in descr:
                # calling capture_log() to capture output from files like- s1,err_s1
                (cmd_status[cmd], cmd_dict[cmd]) = self.capture_log(session_name, cmd, cmdtype)

            count = 0
            for cmd in descr:
                count = count + 1
                if cmd_status[cmd] == "Failed":
                    svalue = "fa fa-times-circle"
                else:
                    svalue = "fa fa-check-circle"
                # calling write_to_js() to write output in test-report.js file
                #self.write_to_js(cmd, count, cmdtype, cmd_dict[cmd], cmd_status[cmd], svalue, session_name)
                display.update_jsfile(cmd, count,cmd,cmdtype, cmd_dict[cmd], cmd_status[cmd],svalue,session_name)
                                 

        except Exception as e:
            logging.debug(e)

    #**************************** open_ssh() *************************************#
    def open_ssh(self,session_name, desc):
        '''
        Authour:-         Shilpa
        Description:-     Method to execute list of commands of type 'ssh' of a given session
        Input Paramters:- Sesson name, list of commands to be executed
        Return:-          None
        '''
        try:
            print("ssh here")
            logging.debug('Active threads are: %s', threading.enumerate())
            abc = [r"C:\Users\akshatha.as\Desktop\plink.exe", "-ssh", "pi@192.168.0.5", "-pw", "raspberry"]
            ss = subprocess.Popen(abc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if os.path.exists(os.path.join(os.getcwd(),"Logs")):
                pass
            else:
                os.mkdir("Logs")

            time.sleep(4)
            for sshitem in desc:
                print("This is ssh script execution!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(sshitem)
                ss.stdin.write(bytes(sshitem + "\n", "ascii"))
                time.sleep(4)
                ss.stdin.flush()
                time.sleep(4)
                logging.debug("Completing Command execution: %s", sshitem)
            ss.stdin.write(bytes("\nexit\n", "ascii"))
            (output, err) = ss.communicate()
            print("output=", output)
            print("err=", err)
            time.sleep(4)
            
            outfile1 = "sshout_" + str(session_name)
            errfile1 = "ssherr_" + str(session_name)

            outfile = os.path.join(os.getcwd(),"Logs",outfile1)
            errfile = os.path.join(os.getcwd(),"Logs",errfile1)

            with open(errfile, "w+") as f:
                f.write(err.decode('utf-8'))
            with open(outfile, "w+") as f:
                f.write(output.decode('utf-8'))

            ssh_status = dict()
            cmdtype = "ssh"
            for cmd in desc:
                # calling capture_log() to capture output from files like- ssh_s1,ssherr_s1
                (ssh_status[cmd], ssh_dict[cmd]) = self.capture_log(session_name, cmd, cmdtype)

            count = 0
            for cmd in desc:
                count = count + 1
                if ssh_status[cmd] == "Failed":
                    svalue = "fa fa-times-circle"
                else:
                    svalue = "fa fa-check-circle"

                # calling write_to_js() to write output in test-report.js file
                display.update_jsfile(cmd, count,cmd,cmdtype, ssh_dict[cmd], ssh_status[cmd], svalue, session_name)

        except Exception as e:
            logging.debug(e)

