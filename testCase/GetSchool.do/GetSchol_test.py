import unittest
import requests
import os,sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\interpace\\check_pswd')
import check_pswd
import time
import json
import GetSchool

result,cookies=check_pswd.check_pswd('10016000','123456')#模拟登陆获取登陆cookies
class GetSchool_Test(unittest.TestCase):
	def setUp(self):
		'''print('测试GetSchool接口中')'''
		
	def test_GetSchoolAssists_success(self):
		print(cookies)
		result=GetSchool.GetSchool(cookies)
		try:
			for a in result['data']['schoolAssists']:
				for key in a:
					self.assertIn(a[key],(31,32,33,10016,1,2,3,6,7,8,9,10,11,12,13,14))
			print('test_GetSchoolAssists_success测试成功')
		except:
			if result['errmsg']=='未登录':
				print('test_GetSchoolAssists_success未登录成功')
			else:
				print('test_GetSchoolAssists_success异常')

	def test_GetSchoolAssists_unlogin(self):
		'''测试未登录情况下的GetSchool接口'''
		result=GetSchool.GetSchool()
		self.assertEqual(result['errmsg'],'未登录')
		print('unlogin测试通过,返回结果是:',result['errmsg'])
	def tearDown(self):
		'''requests.session().close()'''
if __name__=='__main__':
	unittest.main()