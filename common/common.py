import os
import sys
from xlrd import open_workbook
from xml.etree import ElementTree
from common.Log import MyLog as Log
import common.configHttp as configHttp
sys.path.append('C:\\Users\\Administrator\\Desktop\\exam_api_test')
localconfighttp = configHttp.ConfigHttp
# 生成日志文件
proDir = os.path.split(os.path.realpath(__file__))[0]
log = Log.get_log()
logger = log.get_logger()


def get_xls(xls_name,sheet_name):
	"""
	读取excel数据，将casename作为key
	"""
	xlsPath = os.path.join(proDir, 'testfile', xls_name)
	file = open_workbook(xlsPath)
	sheet = file.sheet_by_name(sheet_name)
	# 最终生成的用例词典
	xls = {}
	# 每一行用例生成一个列表
	list = []
	# 首行列表
	first_line = []
	nrows = sheet.nrows
	# 获取每行的值
	for i in range(nrows):
		if sheet.row_values(i)[0] != u'case_name':
			list.append(sheet.row_values(i))
	first_line.append(sheet.row_values(0))
	for test_case in list:
		row_dict = {}
		for cell in range(0, len(first_line[0])):
			row_dict[first_line[0][cell]] = test_case[cell]
		xls[test_case[0]] = row_dict
	return xls


database = {}


def set_xml():
	if len(database) == 0:
		sqlpath = os.path.join(proDir, 'testfile', 'Sql.xml')
		tree = ElementTree.parse(sqlpath)
		for db in tree.findall('database'):
			db_name = db.get("name")
			table = {}
			for table in db.getchildren():
				table_name = table.get("name")
				# print(table_name)
				sql = {}
				for data in table.getchildren():
					sql_id = data.get("id")
					# print(data.text)
					sql[sql_id] = data.text
				# print(sql)
				table = {table_name: sql}
				# table[table_name]=sql
				print(table)
			database[db_name] = table
			print(database)


def get_xml_dict(database_name, table_name):
	set_xml()
	xml_dict = database.get(database_name).get(table_name)
	return xml_dict


def get_sql(database_name, table_name, sql_id):
	db = get_xml_dict(database_name, table_name)
	sql = db.get(sql_id)
	return sql


