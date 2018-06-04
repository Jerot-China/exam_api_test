import requests


def Login(username,password):
	base_url = "http://192.168.1.10:8705/CheckPwd.do"
	params = 'json={"loginName":'+username + ',' + '"pwd" :'+password+'}'
	headers = {
				'Accept': 'application/json, text/plain, */*',
				'Accept-Encoding':'gzip, deflate, sdch',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
				'Referer': 'http://192.168.1.10:8705/template/login.html'
		}
	s = requests.session()
	r = s.get(base_url, params=params, headers=headers)
	result = r.json()
	
	if result['errno'] == 0:
		cookies = r.cookies
		return result, cookies
	else:
		return result
