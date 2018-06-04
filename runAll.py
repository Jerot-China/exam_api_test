import unittest
import HTMLTestRunner
from common.Log import MyLog as Log
import readconfig
import os
from common.configDB import MyDb


class ALLTest:
    def __init__(self):
        global resultpath, log, logger
        log = Log.get_log()
        logger = log.get_logger()
        resultpath = log.get_report_path()
        self.case_list_file = os.path.join(readconfig.proDir, 'test_case_list.txt')
        self.case_file = os.path.join(readconfig.proDir, 'testCase')
        self.case_list = []

    def set_case_list(self):
        """定义用例列表"""
        fb = open(self.case_list_file)
        for value in fb.readlines():
            # 将每一行字符串化
            data = str(value)
            # 字符串不为空，并且不是以#开头的，就将他加入caselist列表中，并且将\n替换成“”
            if data != '' and not data.startswith("#"):
                self.case_list.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.case_list:
            # 获取具体的用例名
            case_name = case.split("/")[-1]
            print(case_name)
            discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        try:
            suite = self.set_case_suite()
            if suite is not None:
                logger.info('*******TEST START*******')
                fp = open(resultpath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试用例', description='测试详情')
                runner.run(suite)
            else:
                logger.info('NO TEST CASE CAN RUN')
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info('*******TEST END*******')
            fp.close()


if __name__ == '__main__':
    db = MyDb()
    db.init_data()
    obj = ALLTest()
    obj.run()

