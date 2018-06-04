import unittest
import requests
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
import time
import json

result,cookies=check_pswd.check_pswd('13909908976','123456')#模拟登陆获取登陆cookies
def Repo_Question_Save(data,cookies):
	base_url='http://192.168.1.10:8705/Repo/Question/Save.do'
	headers={
			'Accept': 'application/json, text/plain, */*',
	}
	s=requests.session()
	r=s.post(base_url,headers=headers,data=data,cookies=cookies)
	result=r.json()
	return result