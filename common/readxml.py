import os
import xml.etree.ElementTree as ET
import readconfig
proDir = readconfig.proDir
xml = os.path.join(proDir, 'common\\testfile\\Sql.xml')


def readxml():
	# 解析xml文件
	tree = ET.parse(xml)
	# 获取根节点
	root = tree.getroot()
	# 遍历根节点
	sql_list = []
	for child in root:
		for children in child:
			for sql in children:
				sql_list.append(sql.text)
	return sql_list

