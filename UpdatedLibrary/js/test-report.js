
            var result = {
              "scenarios" : [ {
                  "scenarioName" : "",
                  "testCases" : [{
          "testCaseName" : "python Homeautomation_Appium.py",
          "steps" : [ {
            "no" : 1,
            "testClassName" : " python Homeautomation_Appium.py ",
            "name" : " cmd ",
            "status" : 1,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551656538,
            "stackTrace" :  "'  File Homeautomation_Appium.py, line 39, in setUpn', 'n',     self.device1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)n, 'n', '  File C:Program FilesPython35libsite-packagesseleniumwebdriverremotewebdriver.py, line 91, in __init__n', 'n', '    self.start_session(desired_capabilities, browser_profile)n', 'n', '  File C:Program FilesPython35libsite-packagesseleniumwebdriverremotewebdriver.py, line 173, in start_sessionn', 'n',     'desiredCapabilities': desired_capabilities,n, 'n', '  File C:Program FilesPython35libsite-packagesseleniumwebdriverremotewebdriver.py, line 231, in executen', 'n', '    response = self.command_executor.execute(driver_command, params)n', 'n', '  File C:Program FilesPython35libsite-packagesseleniumwebdriverremoteremote_connection.py, line 395, in executen', 'n', '    return self._request(command_info[0], url, body=data)n', 'n', '  File C:Program FilesPython35libsite-packagesseleniumwebdriverremoteremote_connection.py, line 463, in _requestn', 'n', '    resp = opener.open(request, timeout=self._timeout)n', 'n', '  File C:Program FilesPython35liburllibrequest.py, line 465, in openn', 'n', '    response = self._open(req, data)n', 'n', '  File C:Program FilesPython35liburllibrequest.py, line 483, in _openn', 'n',     '_open', req)n, 'n', '  File C:Program FilesPython35liburllibrequest.py, line 443, in _call_chainn', 'n', '    result = func(*args)n', 'n', '  File C:Program FilesPython35liburllibrequest.py, line 1268, in http_openn', 'n', '    return self.do_open(http.client.HTTPConnection, req)n', 'n', '  File C:Program FilesPython35liburllibrequest.py, line 1242, in do_openn', 'n', '    raise URLError(err)n', 'n', 'urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>n', 'n', 'n', 'n', '----------------------------------------------------------------------n', 'n', 'Ran 1 test in 1.048sn', 'n', 'n', 'n', 'FAILED (errors=1)n', 'n', 'En', 'n', '======================================================================n', 'n', 'ERROR: testscript (__main__.cpaas_pyTest)n', 'n', '----------------------------------------------------------------------n', 'n', 'Traceback (most recent call last):n', 'n', '  File Homeautomation_AWS_API.py, line 50, in testscriptn', 'n', '    ss = subprocess.Popen(abc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)n', 'n', '  File C:Program FilesPython35libsubprocess.py, line 950, in __init__n', 'n', '    restore_signals, start_new_session)n', 'n', '  File C:Program FilesPython35libsubprocess.py, line 1220, in _execute_childn', 'n', '    startupinfo)n', 'n', 'FileNotFoundError: [WinError 2] The system cannot find the file specifiedn', 'n', 'n', 'n', '----------------------------------------------------------------------n', 'n', 'Ran 1 test in 3.760sn', 'n', 'n', 'n', 'FAILED (errors=1)n', 'n', '  File jiraisuuecreator.py, line 1n', 'n', '    int i = 1n', 'n', '        ^n', 'n', 'SyntaxError: invalid syntaxn', 'n', 'Traceback (most recent call last):n', 'n', '  File Pota_orches.py, line 33, in <module>n', 'n', '    main()n', 'n', '  File Pota_orches.py, line 24, in mainn', 'n', '    client.connect(52.10.165.197, 8181)n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 686, in connectn', 'n', '    return self.reconnect()n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 808, in reconnectn', 'n', '    sock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))n', 'n', '  File C:Program FilesPython35libsocket.py, line 711, in create_connectionn', 'n', '    raise errn', 'n', '  File C:Program FilesPython35libsocket.py, line 702, in create_connectionn', 'n', '    sock.connect(sa)n', 'n', 'TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respondn', 'n'" ,
            "exceptionMessage" : "Test Logs",
            "screenShots" : [ ],
            "statusValue" : " Failed ",
            "statusIcon" : "fa fa-times-circle",
            "session" : " s1 "
          } ]
        },{
          "testCaseName" : "python Homeautomation_AWS_API.py",
          "steps" : [ {
            "no" : 2,
            "testClassName" : " python Homeautomation_AWS_API.py ",
            "name" : " cmd ",
            "status" : 1,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551656538,
            "stackTrace" :  "'  File Homeautomation_AWS_API.py, line 50, in testscriptn', 'n', '    ss = subprocess.Popen(abc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)n', 'n', '  File C:Program FilesPython35libsubprocess.py, line 950, in __init__n', 'n', '    restore_signals, start_new_session)n', 'n', '  File C:Program FilesPython35libsubprocess.py, line 1220, in _execute_childn', 'n', '    startupinfo)n', 'n', 'FileNotFoundError: [WinError 2] The system cannot find the file specifiedn', 'n', 'n', 'n', '----------------------------------------------------------------------n', 'n', 'Ran 1 test in 3.760sn', 'n', 'n', 'n', 'FAILED (errors=1)n', 'n', '  File jiraisuuecreator.py, line 1n', 'n', '    int i = 1n', 'n', '        ^n', 'n', 'SyntaxError: invalid syntaxn', 'n', 'Traceback (most recent call last):n', 'n', '  File Pota_orches.py, line 33, in <module>n', 'n', '    main()n', 'n', '  File Pota_orches.py, line 24, in mainn', 'n', '    client.connect(52.10.165.197, 8181)n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 686, in connectn', 'n', '    return self.reconnect()n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 808, in reconnectn', 'n', '    sock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))n', 'n', '  File C:Program FilesPython35libsocket.py, line 711, in create_connectionn', 'n', '    raise errn', 'n', '  File C:Program FilesPython35libsocket.py, line 702, in create_connectionn', 'n', '    sock.connect(sa)n', 'n', 'TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respondn', 'n'" ,
            "exceptionMessage" : "Test Logs",
            "screenShots" : [ ],
            "statusValue" : " Failed ",
            "statusIcon" : "fa fa-times-circle",
            "session" : " s1 "
          } ]
        },{
          "testCaseName" : "python jiraisuuecreator.py",
          "steps" : [ {
            "no" : 3,
            "testClassName" : " python jiraisuuecreator.py ",
            "name" : " cmd ",
            "status" : 1,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551656538,
            "stackTrace" :  "'  File jiraisuuecreator.py, line 1n', 'n', '    int i = 1n', 'n', '        ^n', 'n', 'SyntaxError: invalid syntaxn', 'n', 'Traceback (most recent call last):n', 'n', '  File Pota_orches.py, line 33, in <module>n', 'n', '    main()n', 'n', '  File Pota_orches.py, line 24, in mainn', 'n', '    client.connect(52.10.165.197, 8181)n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 686, in connectn', 'n', '    return self.reconnect()n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 808, in reconnectn', 'n', '    sock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))n', 'n', '  File C:Program FilesPython35libsocket.py, line 711, in create_connectionn', 'n', '    raise errn', 'n', '  File C:Program FilesPython35libsocket.py, line 702, in create_connectionn', 'n', '    sock.connect(sa)n', 'n', 'TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respondn', 'n'" ,
            "exceptionMessage" : "Test Logs",
            "screenShots" : [ ],
            "statusValue" : " Failed ",
            "statusIcon" : "fa fa-times-circle",
            "session" : " s1 "
          } ]
        },{
          "testCaseName" : "python Pota_orches.py "cd /home/pi/Desktop/New/AWS | sudo python3 DeviceComp.py"",
          "steps" : [ {
            "no" : 4,
            "testClassName" : " python Pota_orches.py "cd /home/pi/Desktop/New/AWS | sudo python3 DeviceComp.py" ",
            "name" : " cmd ",
            "status" : 1,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551656538,
            "stackTrace" :  "'  File Pota_orches.py, line 33, in <module>n', 'n', '    main()n', 'n', '  File Pota_orches.py, line 24, in mainn', 'n', '    client.connect(52.10.165.197, 8181)n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 686, in connectn', 'n', '    return self.reconnect()n', 'n', '  File C:Program FilesPython35libsite-packagespahomqttclient.py, line 808, in reconnectn', 'n', '    sock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))n', 'n', '  File C:Program FilesPython35libsocket.py, line 711, in create_connectionn', 'n', '    raise errn', 'n', '  File C:Program FilesPython35libsocket.py, line 702, in create_connectionn', 'n', '    sock.connect(sa)n', 'n', 'TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respondn', 'n'" ,
            "exceptionMessage" : "Test Logs",
            "screenShots" : [ ],
            "statusValue" : " Failed ",
            "statusIcon" : "fa fa-times-circle",
            "session" : " s1 "
          } ]
        }
            ],
            "nativeReports" : [ ],
            "metrics" : {
              "total" : 4,
              "passed" : 0,
              "failed" : 4,
              "skipped" : 0,
              "startTimeInMillis" : 1465551628147,
              "endTimeInMillis" : 1465551886340
             
            }
          } ],
          "metrics" : {
            "total" : 4,
            "passed" : 0,
            "failed" : 4,
            "skipped" : 0,
            "startTimeInMillis" : 1465551628147,
            "endTimeInMillis" : 1465551886340
           
          }
        }

            