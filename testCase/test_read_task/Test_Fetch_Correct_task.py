import unittest
import requests
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
import time
import json
import FetchCorrectTask
import SaveCorrectResult
import GetCorrectStaByTeacher
result,cookies=check_pswd.check_pswd('10031108','123456')

class Task_taskRead(unittest.TestCase):
	def setUp(self):
		'''没什么用'''
		self.examId=50004699
	def test_success(self):
		GetCorrectStaByTeacher_data={
				'examId':self.examId
		}
		#获取这场考试的itemid  并将第一场传给Fetch接口
		itemIds=GetCorrectStaByTeacher.GetCorrectStaByTeacher(params=GetCorrectStaByTeacher_data,cookies=cookies)
		itemIds=iter(itemIds)
		itemId=next(itemIds)
		print(itemId)

		while True:
			taskId=FetchCorrectTask.FetchCorrectTask(examId=self.examId,itemId=itemId,cookies=cookies)#调用接口，获取返回的taskid作为save接口的参数			
			Save_data={
				'taskId':taskId,
				'score':1,
				'markinfo':'',
				'excellentAnswer':0,
				'typicalWrongAnswer':0
			}
			result=SaveCorrectResult.SaveCorrectResult(data=Save_data,cookies=cookies)#调用save接口
			print(result)
			sleep(1)

	def tearDown(self):
		'''print(测试完成)'''
if __name__=='__main__':
	unittest.main()
