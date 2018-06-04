import unittest
import requests
import time
import sys
import common.Login as Login
from common.Log import MyLog as Log
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test')
login_result, cookies = Login.Login('10013000', '123456')


class CreateExamTest(unittest.TestCase):

	def setUp(self):
		self.base_url = 'http://192.168.1.10:8705/CreateExam.do'
		self.headers = {
				'Connection': 'keep-alive',
				'Referer':'http://192.168.1.10:8705/',
				'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Accept-Encoding': 'gzip, deflate',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
				'Accept': 'application/json, text/plain, */*',
				'Content-Length': '496',
				'Host': '192.168.1.10:8705'
		}
		self.log = Log.get_log()
		self.logger = self.log.get_logger()

	def test_CreteExam_success(self):
		"""测试请求发送成功"""
		self.time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
		self.data = 'json={"exam":{"examTime":"'+self.time+'","examType":1,"grade":31,"name":"当前时间",\
		"schoolId":10013,"score":null,"subjectId":1,"subjectName":"语文","dataSource":1},\
		"examRanges":[{"rangeValue":335989,"rangeText":"高一7班","rangeType":2}],\
		"subjectIds":[1]}'.encode("utf-8").decode("latin1")
		r=requests.post(self.base_url, data=self.data, cookies=cookies, headers=self.headers)
		self.result = r.json()
		self.assertEqual(self.result['errmsg'], 'OK')

	def test_CreteExam_failed(self):
		"""测试请求发送失败"""
		self.time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
		self.data = '{"exam":{"examTime":"'+self.time+'","examType":1,"grade":31,"name":"当前时间",\
		"schoolId":10013,"score":null,"subjectId":1,"subjectName":"语文","dataSource":1},\
		"examRanges":[{"rangeValue":335989,"rangeText":"高一7班","rangeType":2}],\
		"subjectIds":[1]}'.encode("utf-8").decode("latin1")
		r = requests.post(self.base_url, data=self.data, cookies=cookies)
		self.result = r.json()

	def tearDown(self):
		if self.result['errmsg'] == 'OK':
			print('请求发送成功', self.result['data'])
		else:
			print('请求发送失败，错误代码为\'%s\',错误详情是\'%s\'' % (self.result['errno'], self.result['errmsg']))


if __name__ == '__main__':
	unittest.main()
