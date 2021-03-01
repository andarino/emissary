#!/usr/bin/python
'''
AUTHOR: __andar1n0__

auto sender of a compressed folder in your pc
Emissary is a script that allows you to schedule sending of a zip archive throught the tor network, the sending is protected under cryptography.
'''
import os
import zipfile
from time import sleep, time
import time
def messenger():
	#preparing the file to send
	new = zipfile.ZipFile('new.zip', 'w')
	new.write('send',compress_type=zipfile.ZIP_DEFLATED)
	new.close()
	#sending through the protonmail

def validate_date(string):
	try: 
		date, hora = string.split("-")
		day, month, year = date.split("/")
		hour, minute = hora.split(":")
		'''!converter the args to int'''
		launch = (day, month, year, hour, minute)
		coocuo(launch)
	except:
		raise
		print("date or hour in inadequate format")
def coocuo(*launch):
	while 1:
		now = time.localtime()
		if (now.tm_year == int(launch[0][2]) and now.tm_mon == int(launch[0][1]) and now.tm_mday == int(launch[0][0]) and now.tm_hour == int(launch[0][3]) and now.tm_min == int(launch[0][4])):
			print("by smoke")	#check messager
			#messenger()
			break	
	#	sleep(30)
	
if __name__=='__main__':
	dateComplete =input('[-] schedule the date and hour (22/5/2012-8:32): ')
	validate_date(dateComplete)
	#clock to count the time (next step) 
