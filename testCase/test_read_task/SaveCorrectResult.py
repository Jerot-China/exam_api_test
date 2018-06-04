import unittest
import requests
import time
import json
def SaveCorrectResult(data,cookies):
	base_url='http://192.168.1.10:8705/SaveCorrectResult.do'
	headers={
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate',
		'User-Agent': 'python-requests/2.18.3'
	}
	s=requests.session()
	r=s.post(base_url,data=data,cookies=cookies,headers=headers)
	result=r.json()
	s.close()
	return result['errmsg']