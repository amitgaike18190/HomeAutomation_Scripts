import paho.mqtt.client as paho
#import json
from subprocess import Popen, PIPE
from socket import gethostname
import sys

def on_connect(client, userdata, flags, rc):
	print("CONNACK received with code %d: " % (rc))

#def on_subscribe(client, userdata, mid, granted_qos):
#	print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
	print("Response: "+str(msg.payload))
	client.disconnect()

def main():
#global output
 print(gethostname().upper())
 
 command =""
 for i in range(1,(len(sys.argv))):
 	command = command + str(sys.argv[i]) + " "

 client = paho.Client()
 client.on_connect = on_connect
 client.connect("52.10.165.197", 8181)
 client.subscribe("PIBANG01/orchestrator/output",qos=1)
 #client.on_subscribe = on_subscribe
 client.on_message = on_message
 
 client.publish("PIBANG01/orchestrator/command", str(command), qos=1)

 client.loop_forever()

main()
