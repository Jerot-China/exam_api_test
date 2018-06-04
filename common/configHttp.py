import requests
import sys
import readconfig
from common.Log import MyLog as Log
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test\\common')
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test')
localreadconfig = readconfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global baseurl, timeout
        baseurl = localreadconfig.get_http('baseurl')
        timeout = localreadconfig.get_http('timeout')
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.url = None
        self.headers = {}
        self.params = {}
        self.data = {}
        self.files = {}

    def set_url(self, url):
        self.url = baseurl+url

    def set_headers(self,headers):
        self.headers = headers

    def set_params(self,params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_files(self,file):
        self.files = file

    # 定义get方法
    def get(self):
        try:
            response=requests.get(self.url,params=self.params,headers=self.headers,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("time out!")
            return None

    # 定义post方法
    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("time out!")
            return None
