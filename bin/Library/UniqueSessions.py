#-----------------------------------------------------------#
# Authour: Shilpa                                           #
# Description : Program to parse Commands.xml file          #
# Date :27-12-2016                                          #
#-----------------------------------------------------------#


#------------------------Python imports---------------------#
import os
import xml.etree.ElementTree as ET

#------------------------Main-------------------------------#
record_dict = dict()

def session():
    '''
    Description:-     Method to Parse given xml file and calculate 'Global Value of sleep'
    Input Paramters:- None
    Return:-          First Record's parsed values in a Tuple (Yet to decide for Dictionary or Multiple list of values)
    '''
    os.chdir(os.getcwd())
    file_path = r'C:\Orchestrator\Commands.xml'
    #file_path = r'C:\Users\shilpa.alagundi\Desktop\Jan 12\Commands.xml'
    record_count = 0

    try:
        #XML Parsing starts here    
        tree = ET.parse(file_path) 
        root = tree.getroot()
        
        # To calculte sleep time
        sleep_time=0
        rep_exp='powershell -command "Start-Sleep -s "'
        
        for record in root:
            record_count+=1
            name = []# To store session ids (ex- s1,s2)
            cmd_name = [] # To store cmd type(ex- cmd/ssh)
            sflag = False
            desc_list = list()# To store list of all commands of a session
            row = 0# To store count of all commands of a record
            d = dict()
            # Parsing Each record here
            for cmd_detail in record.findall('CommandDetail'):               
                sflag = False
                se = cmd_detail.find('Session').text
                if se not in name:
                    name.append(se)
                    sflag = True
                    d[se]=list()

                cmdtype = cmd_detail.find('CommandType').text
                if sflag:
                    cmd_name.append(cmdtype)
                elif sflag and (cmdtype not in cmd_name):
                    cmd_name.append(cmdtype)
                else:
                    pass
                desc = cmd_detail.find('Description').text
                
                # Processing sleep time for cmd/ssh command
                if((desc.split(" ")[0]) == "sleep"):
                    if cmdtype == "cmd":
                        print("Global Value of sleep: ",str(sleep_time))
                        sleep_time = sleep_time + int(desc.split(" ")[1])
                        d[se].append(rep_exp + str(sleep_time))
                        desc_list.append(rep_exp + str(sleep_time))
                    elif cmdtype == "ssh":
                        print("Global Value of sleep: ",str(sleep_time))
                        sleep_time = sleep_time + int(desc.split(" ")[1])
                        d[se].append("sleep "+str(sleep_time))
                        desc_list.append("sleep "+str(sleep_time))
                    else:
                        d[se].append(desc.split(" ")[1])
                        desc_list.append(desc.split(" ")[1])
                else:
                    d[se].append(desc)
                    desc_list.append(desc)
                                                    
                row = row + 1

            #print("d=",d)
            a = list()
            for key in d:
                a.append(d[key])
            #print("a=",a)
            #record_dict["Record"+str(record_count)] = (row, name, desc_list, cmd_name)
            record_dict["Record"+str(record_count)] = (row, name, a, cmd_name)
            #print("next")
    except Exception as e:
        print(e)
    print("Total Number of Records = ",record_count)
    row, name, s, cmd_name = record_dict["Record1"]
    

    return row, name, s, cmd_name

if __name__=='__main__':
    print(session())
    
