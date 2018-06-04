import sys
sys.path.append('../db_fixture')
from mysql_db import DB
datas={
	't_school_assist':[{'id':6,'school_id':10016,'subject_id':1,'grade_num':31},
						{'id':7,'school_id':10016,'subject_id':2,'grade_num':31},
						{'id':8,'school_id':10016,'subject_id':3,'grade_num':31},
						{'id':9,'school_id':10016,'subject_id':1,'grade_num':32},
						{'id':10,'school_id':10016,'subject_id':2,'grade_num':32},
						{'id':11,'school_id':10016,'subject_id':3,'grade_num':32},
						{'id':12,'school_id':10016,'subject_id':1,'grade_num':33},
						{'id':13,'school_id':10016,'subject_id':2,'grade_num':33},
						{'id':14,'school_id':10016,'subject_id':3,'grade_num':33}]
}
def init_data():
	db=DB()
	for table,data in datas.items():
		db.clear(table,'school_id',str(10016))
		for d in data:
			for key in d:
				d[key]="'"+str(d[key])+"'"
			key=','.join(d.keys())
			value=','.join(d.values())
			db.insert(table,key,value)	
	db.close()

if __name__=='__main__':
	init_data()	