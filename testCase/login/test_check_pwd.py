import unittest
import xml.dom.minidom
import common.Login as Login
dom = xml.dom.minidom.parse('C:\\Users\\Administrator\\Desktop\\exam_api_test\\testCase\\login\\check_pwd.xml')
root = dom.documentElement


class CheckPwdTest(unittest.TestCase):
	def setUp(self):
		self.headers = {
				'Accept': 'application/json, text/plain, */*',
				'Accept-Encoding': 'gzip, deflate, sdch',
				'Accept-Language': 'zh-CN,zh;q=0.8',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
				Chrome/50.0.2661.102 Safari/537.36',
				'Referer': 'http://192.168.1.10:8705/template/login.html'
		}

	def test_login_pwd_error(self):
		"""密码错误"""
		logins = root.getElementsByTagName('password_error')
		username = logins[0].getAttribute('username')
		password = logins[0].getAttribute('password')
		self.result = Login.Login(username, password)
		self.assertEqual(self.result['errmsg'], "登录失败")
		self.assertEqual(self.result['errno'], 1001)

	def test_account_error(self):
		"""测试账号不存在"""
		logins = root.getElementsByTagName('account_error')
		username = logins[0].getAttribute('username')
		password = logins[0].getAttribute('password')
		self.result = Login.Login(username,password)
		self.assertEqual(self.result['errmsg'], '登录失败')
		self.assertEqual(self.result['errno'], 1001)

	def test_login_success(self):
		"""测试登录成功"""
		logins = root.getElementsByTagName('success')
		username = logins[0].getAttribute('username')
		password = logins[0].getAttribute('password')
		# 分别赋值结果和返回的cookie信息
		self.result, self.cookies = Login.Login(username, password)
		# cookies = r.cookies
		# cookies=(';'.join(['='.join(item) for item in cookies.items()]))
		self.assertEqual(self.result['errmsg'], 'OK')
		self.assertEqual(self.result['errno'], 0)
		
	def tearDown(self):
		print('测试通过')


if __name__ == '__main__':
	unittest.main()
