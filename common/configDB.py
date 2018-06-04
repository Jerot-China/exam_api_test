import pymysql
import readconfig
from common.Log import MyLog as Log
import common.readxml as readxml
local_read_config = readconfig.ReadConfig()


class MyDb:
	global host, port, user, password, db, config
	host = local_read_config.get_db('host')
	port = local_read_config.get_db('port')
	user = local_read_config.get_db('user')
	password = local_read_config.get_db('password')
	db = local_read_config.get_db('db_name')
	config = {
		'host': str(host),
		'port': int(port),
		'user': user,
		'password': password,
		'db': db,
	}

	def __init__(self):
		log = Log.get_log()
		logger = log.get_logger()

	def connect_db(self):
		try:
			self.db = pymysql.connect(**config)
			self.cursor = self.db.cursor()
		except Exception as e:
			logging.error(str(e))
		else:
			print('数据库连接成功')

	def init_data(self):
		try:
			self.connect_db()
			self.sql_list = readxml.readxml()
			for sql in self.sql_list:
				print(sql)
				self.cursor.execute(sql)
			self.db.commit()
		except Exception as e:
			logging.info('执行sql语句出错')
			logging.error(str(e))

		try:
			self.db.close()
		except Exception as error:
			logging.info('数据库关闭出现异常')
			logging.error(str(e))
		finally:
			print('数据初始化成功')


if __name__ == '__main__':
	db = MyDb()
	db.init_data()

