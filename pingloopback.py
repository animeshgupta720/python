#!/usr/bin/env python



#from flask import Flask,render_template, Markup
import json
from napalm import get_network_driver
import time
import threading
import datetime

#import napalm

'''f = open('ospf1.cfg','r')
var = f.read()
print(var)'''

#myLoopback = "30.0.0.1"
#myAid = "0"
driver = get_network_driver('ios')
iosvl2 = driver('198.51.100.3','lab','lab123')
iosvl2.open()
destination=["10.0.0.1","20.0.0.1","30.0.0.1","40.0.0.1"]

for ip in destination:

	ospf_getconfig = iosvl2.ping(ip)
	time.sleep(3)

	value = (ospf_getconfig["success"])

	if (value["packet_loss"])<2:
		print("IP {} is configured in network and is reachable".format(ip))	
	else:
		print("IP {} is not reachable. Please check.".format(ip))
	
