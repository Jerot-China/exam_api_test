import unittest
import requests
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
import time
import json
def GetSchool(cookies=0):
	base_url='http://192.168.1.10:8705/GetSchool.do'
	headers={
			'Accept': 'application/json, text/plain, */*',
	}
	s=requests.session()
	if cookies:
		r=s.get(base_url,headers=headers,cookies=cookies)
		#result=r.json()
	else:
		r=s.get(base_url,headers=headers)
	result=r.json()
	s.close()
	return result
