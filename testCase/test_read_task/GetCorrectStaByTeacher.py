import unittest
import requests
import time
import json

def GetCorrectStaByTeacher(params,cookies):
	base_url='http://192.168.1.10:8705/GetCorrectStatByTeacher.do'
	s=requests.session()
	r=s.get(base_url,params=params,cookies=cookies)
	result=r.json()
	itemIds=[]
	for i in result['data'][0]['items']:
		itemID=i['itemId']
		itemIds.append(itemID)
	s.close()
	return itemIds