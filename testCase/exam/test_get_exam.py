import unittest
import requests
import sys
from common.Log import MyLog as Log
import common.Login as Login
from common.common import get_xls
import logging
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test')
login_result, cookies = Login.Login('19900200002', '123456')
xls = get_xls('get_exam.xlsx', 'Sheet1')


class TestGetExam(unittest.TestCase):

	def setUp(self):
		self.headers = {
				'content-type': 'application/json'
		}
		log = Log.get_log()
		logger = log.get_logger()

	def test_GetExam_success(self):
		"""测试请求成功"""
		try:
			self.xls = xls['测试通过']
			self.base_url = self.xls['base_url']
			self.data = self.xls['data']
			self.errorno = self.xls['errno']
			self.classid = self.xls['classid']
			self.subjectid = self.xls['subjectId']
			self.s = requests.Session()
			r = self.s.get(self.base_url, params=self.data)
			self.result = r.json()
			self.assertEqual(self.result['errno'], self.errorno)
			# 判断考试学科是否正确
			self.assertEqual(self.result['data']['exam']['subjectId'], self.subjectid)
			# 判断年级是否正确
			self.assertEqual(self.result['data']['exam']['grade'], self.classid)
		except Exception as error:
			logging.error(error)
		else:
			print('test_success测试成功')

	def test_GetExam_null_id(self):
		"""测试发送请求时，examId为空"""
		try:
			self.xls = xls['examId为空']
			self.base_url = self.xls['base_url']
			self.data = self.xls['data']
			self.errorno = self.xls['errno']
			self.message = self.xls['message']
			self.s = requests.Session()
			r = self.s.get(self.base_url, params=self.data)
			self.result = r.json()
			self.assertEqual(self.result['errno'], self.errorno )
			self.assertEqual(self.message, '异常: null')
		except Exception as error:
			logging.error(error)
		else:
			print('test_GetExam_null_id测试通过')
	
	def test_GetExam_no_parameter(self):
		"""测试请求为空的情况"""
		try:
			self.base_url = xls['数据为空']['base_url']
			self.data = xls['数据为空']['data']
			self.errorno = xls['数据为空']['errno']
			self.message = xls['数据为空']['message']
			self.s = requests.Session()
			r = self.s.get(self.base_url, params=self.data)
			self.result = r.json()
			self.assertEqual(self.result['errno'], self.errorno)
			self.assertEqual(self.result['errmsg'], self.message)
		except Exception as error:
			logging.error(error)
		else:
			print('Test_Get_Exam_no_parameter测试通过')

	def test_GetExam_examId_nonentity(self):
		"""传入的examId不存在的情况"""
		try:
			self.base_url = xls['examId不存在']['base_url']
			self.data = xls['examId不存在']['data']
			self.errorno = xls['examId不存在']['errno']
			self.s = requests.Session()
			r = self.s.get(self.base_url, params=self.data)
			self.result = r.json()
			self.assertEqual(self.result['errno'], 0)
			self.assertEqual(self.result['data'], {})
		except Exception as error:
			logging.error(error)
		else:
			print('test_GetExam_examId_nonentity测试通过')

	def tearDown(self):
		self.s.close()


if __name__ == '__main__':
	unittest.main()
