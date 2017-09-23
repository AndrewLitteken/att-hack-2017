#! /usr/bin/env python

from WebInterfaces.WebHost.WebHost import *
import random
import threading
import time

import traceback

class JeffyWebInterface(WebInterface):
	def __init__(self,port,rtkd):
		self.port = port
		self.host = WebHost(self.port,staticdir="WebInterfaces/static",staticindex="jeffy.html")
		self.rtkd = rtkd
		
		self.connect('/all_users/',			'ALL_USERS',	'GET')
		self.connect('best_users/:cnt',		'BEST_USERS',	'GET')
		self.connect('worst_users/:cnt',	'WORST_USERS',	'GET')
	
	def ALL_USERS(self):
		"""return stats on all users"""
		output = {'result':'success'}
		try:
			pass
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
			output['traceback'] = traceback.format_exc()
		return json.dumps(output)
	
	def BEST_USERS(self,cnt):
		"""return stats on the best users"""
		output = {'result':'success'}
		try:
			pass
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
			output['traceback'] = traceback.format_exc()
		return json.dumps(output)
	
	def WORST_USERS(self,cnt):
		"""return stats on the worst users"""
		output = {'result':'success'}
		try:
			pass
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
			output['traceback'] = traceback.format_exc()
		return json.dumps(output)
	
	def startWebHost(self):
		self.host.start_service()
	
	def stopWebHost(self):
		self.host.stop_service()
	
	def startRESTinterface(self):
		self.thr = threading.Thread(target=self.startWebHost)
		self.thr.daemon = True
		self.thr.start()
		return self.thr
	
	def stopRESTinterface(self):
		self.stopWebHost()