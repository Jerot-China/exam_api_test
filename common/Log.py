import logging
from datetime import datetime
import threading
import sys
import readconfig
import os
sys.path.append('C://Users//Administrator//Desktop//exam_api_test')


class Log:
	def __init__(self):
		global resltpath, logpath, proDir
		proDir = readconfig.proDir
		resultpath = os.path.join(proDir, "result")
		if not os.path.exists(resultpath):
			os.mkdir(resultpath)
		logpath = os.path.join(resultpath, str(datetime.now().strftime('%Y-%m-%d')))
		if not os.path.exists(logpath):
			os.mkdir(logpath)
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		self.handler = logging.FileHandler(os.path.join(logpath, 'output.log'))
		self.formatter = logging.Formatter("%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - \
		%(message)s", "%Y-%m-%d %H:%M:%S")
		self.handler.setFormatter(self.formatter)
		self.logger.addHandler(self.handler)

	# 封装方法返回log
	def get_logger(self):
		return self.logger

	def get_report_path(self):
		"""获取报告文件路径"""
		report_path = os.path.join(logpath, 'report.html')
		return report_path

	def get_log_path(self):
		"""获取日志路径"""
		return logPath


# 将log放进一个线程中
class MyLog:
	log = None
	mutex = threading.Lock()

	def __init__(self):
		pass

	@staticmethod
	def get_log():

		if MyLog.log is None:
			MyLog.mutex.acquire()
			MyLog.log = Log()
			MyLog.mutex.release()
		return MyLog.log


if __name__ == '__main__':
	log = MyLog.get_log()
	logger = log.get_logger()
	logger.debug("test debug")
	logger.info("test info")
