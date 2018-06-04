import unittest
import requests
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
import time
import json
import HTMLTestRunner

login_result,cookies=check_pswd.check_pswd('10016000','123456')
def GetExamAssist(self,data):
	self.headers={
				'content-type': 'application/json'
		}
	self.base_url='http://192.168.1.10:8705/GetExamByAssist.do'
	self.s = requests.Session()
	r=self.s.post(base_url,headers=self.headers,data=data)

