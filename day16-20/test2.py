#encoding=utf-8
import unittest
from selenium import webdriver
import time


class DuApp(unittest.TestSuite):
    def setUp(self):
        # 启动FireFox浏览器
        self.driver = webdriver.Firefox(executable_path='D:\\geckodriver')

    def testSoGou(self):
        # 访问毒首页
        self.driver.get("https://sogou.com/")
        # 情况搜索框内容
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys(u"毒球鞋")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        assert u"球鞋交易" in self.driver.page_source, "页面不存在要寻找的关键字"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
