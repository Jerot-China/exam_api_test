from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
# ===========读取 db_config.ini===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))# 获取自身文件目录的上级目录
base_dir = base_dir.replace('\\', '/')# 将\替换成/
cf = cparser.ConfigParser()
cf.read(base_dir+'/db_config.ini')
host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")


# 封装Mysql数据库基本操作
class DB:
	def __init__(self):
		try:
			self.conn = connect(
				host=host,
				user=user,
				password=password,
				db=db,
				charset='utf8',
				cursorclass=cursors.DictCursor)
			print('数据库链接成功')
		except OperationalError as e:
			print('Mysql Error %d:%s' % (e.args[0], e.args[1]))

	# 清除表数据
	def clear(self, table_name, key, value):
		real_sql = "delete from "+table_name+" where "+key+"="+"\'"+value+"\'"+";"
		with self.conn.cursor() as cursor:
			print('成功创建游标')
			cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
			cursor.execute(real_sql)
		self.conn.commit()
		print('数据删除成功')

	# 插入数据
	def insert(self, table_name, key, value):
		real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"+";"
		with self.conn.cursor() as cursor:
			cursor.execute(real_sql)
		self.conn.commit()
		print(real_sql)

	# 关闭数据库
	def close(self):
		self.conn.close()


if __name__ == '__main__':
	db = DB()
	# table_name=[]
	# for a in table_name:
	# 	db.clear(table_name)
	# 	db.insert(table_name)
	# 	db.close()
