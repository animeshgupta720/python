#!/usr/bin/env python

import json


from flask import Flask,render_template, Markup, request
import json
from napalm import get_network_driver
import time
import threading
import datetime
from prettytable import PrettyTable

#condition=0
	


def validipcheck(value):
	list1 = value.split('.')	
	condition = 0
	if len(list1)==4:

		for i in list1:
		#print(i)
			if int(i)>=0 and int(i)<=255:
				condition=condition+1

		if condition!=4:
				print("{} is not a valid IP address".format(value))
		else:
				print("{} number is valid IP address".format(value))

#iplist = []
#intlist = []
#zip = zip(iplist, intlist)

def interfaceprint():
	#zip = zip(iplist, intlist)
	iplist = ["198.51.100.3","172.16.1.3","172.16.1.2","172.16.1.4"]
	intlist = []
	#zip = zip(iplist, intlist)

	for ip in iplist:
			driver = get_network_driver('ios')
			iosvl2 = driver(ip,'lab','lab123')
			iosvl2.open()
			print("The active interfaces for IP {} are:".format(ip))

    			result = iosvl2.get_interfaces_ip()
			print(result.keys())
			intlist.append(result.keys())
    			iosvl2.close()


	'''table = PrettyTable(['IP','Interfaces'])

	#zip = zip(iplist, intlist)

	for rows in zip:
		table.add_row([rows[0],rows[1]])
	print(table)'''
interfaceprint()
