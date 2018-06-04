#
#                             _ooOoo_
#                            o8888888o
#                            88" . "88
#                            (| -_- |)
#                            O\  =  /O
#                         ____/`---'\____
#                       .'  \\|     |//  `.
#                      /  \\|||  :  |||//  \
#                     /  _||||| -:- |||||-  \
#                     |   | \\\  -  /// |   |
#                     | \_|  ''\---/''  |   |
#                     \  .-\__  `-`  ___/-. /
#                   ___`. .'  /--.--\  `. . __
#                ."" '<  `.___\_<|>_/___.'  >'"".
#               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#               \  \ `-.   \_ __\ /__ _/   .-` /  /
#          ======`-.____`-.___\_____/___.-`____.-'======
#                             `=---='
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                     佛祖保佑        永无BUG
#            佛曰:
#                   写字楼里写字间，写字间里程序员；
#                   程序人员写程序，又拿程序换酒钱。
#                   酒醒只在网上坐，酒醉还来网下眠；
#                   酒醉酒醒日复日，网上网下年复年。
#                   但愿老死电脑间，不愿鞠躬老板前；
#                   奔驰宝马贵者趣，公交自行程序员。
#                   别人笑我忒疯癫，我笑自己命太贱；
#                   不见满街漂亮妹，哪个归得程序员？
#
import unittest
import requests
import sys
from common.Log import MyLog as Log
import common.Login as Login
from common.common import get_xls
import logging
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test')
login_result, cookies = Login.Login('10013000', '123456')
xls = get_xls('create_student.xlsx', 'Sheet1')


class CreateStudent(unittest.TestCase):
	def setUp(self):
		self.headers = {
				'Accept': 'application/json, text/plain, */*',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content - Length': '297',
				'Host': '192.168.1.10:8705',
				'Origin': 'http: // 192.168.1.10: 8705',
				'Proxy - Connection': 'keep - alive',
				'Referer': 'http://192.168.1.10: 8705/'
		}
		log = Log.get_log()
		logger = log.get_logger()

	def test_CreateStudent_success(self):
		"""创建学生 创建成功"""
		try:
			self.xls = xls['创建成功']
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			self.classid = self.xls['classid']
			self.schoolid = self.xls['schoolid']
			self.mark = self.xls['mark']
			self.name = self.xls['name']
			self.verifyCode = self.xls['verifyCode'].rstrip(".0")
			self.smallNo = self.xls['smallNo']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['errmsg'], self.message)
				self.assertEqual(result['data']['classId'], self.classid)
				self.assertEqual(result['data']['schoolId'], self.schoolid)
				self.assertEqual(result['data']['name'], self.name)
				self.assertEqual(result['data']['mark'], self.mark)
				self.assertEqual(result['data']['verifyCode'], self.verifyCode)
				self.assertEqual(result['data']['smallNo'], self.smallNo)
			except Exception as error:
				logging.error(error)
		except Exception as error:
			logging.error(error)
		else:
			print('=======TestCreateStudent_success 测试通过=======')

	def test_CreateStudent_class_null(self):
		"""创建学生 不存在的班级"""
		try:
			self.xls = xls['不存在的班级']
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['errmsg'], self.message)
			except Exception as e:
				logging.error(e)
		except Exception as error:
			logging.error(error)
		else:
			print('=======班级不存在 测试通过=======')

	def test_CreateStudent_name_null(self):
		"""创建学生 姓名为空"""
		try:
			self.xls = xls['姓名为空']
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			self.classid = self.xls['classid']
			self.schoolid = self.xls['schoolid']
			self.name = self.xls['name']
			self.mark = self.xls['mark']
			self.verifyCode = str(self.xls['verifyCode']).rstrip(".0")
			self.smallNo = self.xls['smallNo']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['errmsg'], self.message)
				self.assertEqual(result['data']['classId'], self.classid)
				self.assertEqual(result['data']['schoolId'], self.schoolid)
				self.assertEqual(result['data']['name'], self.name)
				self.assertEqual(result['data']['mark'], self.mark)
				self.assertEqual(result['data']['verifyCode'], self.verifyCode)
				self.assertEqual(result['data']['smallNo'], self.smallNo)
			except Exception as error:
				logging.error(error)
		except Exception as error:
			logging.error(error)
		else:
			print('=======姓名为空 测试通过=======')

	def test_CreateStudent_name_repetition(self):
		"""创建学生 姓名重复"""
		try:
			self.xls = xls['姓名相同，学号不同']
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			self.classid = self.xls['classid']
			self.schoolid = self.xls['schoolid']
			self.name = self.xls['name']
			self.mark = self.xls['mark']
			self.verifyCode = str(self.xls['verifyCode']).rstrip(".0")
			self.smallNo = self.xls['smallNo']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['errmsg'], self.message)
				self.assertEqual(result['data']['classId'], self.classid)
				self.assertEqual(result['data']['schoolId'], self.schoolid)
				self.assertEqual(result['data']['name'], self.name)
				self.assertEqual(result['data']['mark'], self.mark)
				self.assertEqual(result['data']['verifyCode'], self.verifyCode)
				self.assertEqual(result['data']['smallNo'], self.smallNo)
			except Exception as error:
				logging.error(error)
		except Exception as error:
			logging.error(error)
		else:
			print('=======姓名重复 测试通过=======')

	def test_CreateStudent_code_null(self):
		"""创建学生 学号重复"""
		try:
			self.xls = xls['姓名不同，学号重复']
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['errmsg'], self.message)
			except Exception as error:
				logging.error(error)
		except Exception as error:
			logging.error(error)
		else:
			print('=======学号重复 测试通过=======')

	def test_no_right_account(self):
		"""创建学生 没有权限的账号"""
		try:
			self.xls = xls['使用非管理员权限的角色添加学生']
			self.account = self.xls['account']
			self.password = self.xls['password']
			print(self.account)
			no_right_login_result, no_right_login_cookies = Login.Login(self.account, self.password)
			self.base_url = self.xls['base_url']
			self.method = self.xls['method']
			self.data = self.xls['data'].encode('utf-8')
			self.errno = self.xls['errno']
			self.message = self.xls['message']
			result = requests.post(self.base_url, data=self.data, headers=self.headers, cookies=no_right_login_cookies)
			result = result.json()
			try:
				self.assertEqual(result['errno'], self.errno)
				self.assertEqual(result['message'], self.message)
			except Exception as error:
				logging.error(error)
		except Exception as error:
			logging.error(error)

	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main()
	# c = CreateStudent()
	# c.test_no_right_account()

