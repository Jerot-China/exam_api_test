import unittest
import requests
import time
import json
import GetCorrectStaByTeacher
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
#登录并且获取首个itemid 并且将所有itemid做成一个迭代器
result,cookies=check_pswd.check_pswd('10031108','123456')
GetCorrectStaByTeacher_data={
				'examId':50004699
		}

itemIds=GetCorrectStaByTeacher.GetCorrectStaByTeacher(params=GetCorrectStaByTeacher_data,cookies=cookies)
itemIds=iter(itemIds)
def FetchCorrectTask(examId,itemId,cookies):
		base_url='http://192.168.1.10:8705/FetchCorrectTask.do'
		s=requests.session()
		data={
			'examId':examId,
			'itemId':itemId
		}
		r=s.post(base_url,data=data,cookies=cookies)
		result=r.json()
		s.close()
		
		if result['data']==None:
			#如果返回的data是null，则获取下一个itemid
			itemId=next(itemIds)
			print(itemId)
			result=FetchCorrectTask(examId=examId,itemId=itemId,cookies=cookies)
			return result			
		else:
			return result['data']['id']