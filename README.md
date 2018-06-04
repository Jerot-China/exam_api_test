###########环境依赖
python v3.6
mysql

###########部署
1.git上下载py3.0+的httptestrunner           /能适应py3.0的httptestrunner需要修改源码，git上有修改后的包
2.pip install Log                          /安装log库
3.pip install requests                     /安装requests库
4.pip install xlrd                         /安装xlrd库
5.pip install pymysql                      /安装pymysql库
6.将项目根目录配置进系统环境变量
7.运行runAll启动项目                        /运行项目

###########目录结构描述
|———README.md                   /help
|———readconfig.py               /读取配置文件
|———test_case_list.txt          /待测测试用例列表，忽略的用例在前面加上#
|———runAll.py                   /运行脚本
|———common                      /该文件夹用来存储通用方法以及测试数据
|   |———testfile                /将测试数据通过excel储存在testfile中，每个excel以对应用例名称命名。将测试用的sql语句放在xml文件中
|   |———common.py               /用来读取和返回测试数据和执行的sql
|   |———configDB.py             /连接并初始数据库
|   |———configHttp.py           /将get和post方法再封装
|   |———Log.py                  /封装Log模块，将日志和报告放在result文件中
|   |———Login.py                /通用的登录方法
|   |———readxml.py              /readxml用来读取xml文件中的sql语句
|———config                      
|   |———config.ini              /配置文件
|———db_fixture
|   |———mysql_db.py             /将insert和delete方法封装
|———rusult                      /运行完runAll产生的log和运行结果，文件夹以年月日命名（20171220）
|———testcase                    /具体的测试用例都在该文件夹下