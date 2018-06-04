#测试成功 
#测试空格数为4个 答案超过4个如 有四个选项ABCD选择了F答案
#测试单选题传了多个答案的情况
#多选题选的答案数量超过总和数量
#多选题选的答案不是多选题规定的答案
#测试判断题答案多选
#测试判断题答案不是T/F
#测试不传入学科ID
#测试传入的学科id不是系统给定的ID
#测试传入的qtype不是系统给定的qtype
#测试传入知识点与所选学科不同的返回结果
#未登录时保存
#调用接口不传data
import unittest
import requests
import time
import json
import repo_question_save
class Repo_Qusetion_Save_Test(unittest.TestCase):
	def setUp(self):
		'''print('正在测试Repo/Qusetion/Save.do接口')'''
	def test_success(self):
		'''测试成功'''
		data={"subjectId":"5","questionNoMain":"","questionNoSub":"","qtype":501,"objective":1,/
		"title":"<p>接口测试题干</p>\n","spaceCount":4,"answer":"B","parse":"<p>接口测试解析</p>\n",/
		"kps":[],"qtag":1,"diff5":5,"qlabels":"2","creator":50042695,"subQuestionTag":0,"id":null}