#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox(executable_path="D:\\geckodriver")
driver.get("https://www.sogou.com/")
driver.find_element_by_id("query").clear()
driver.find_element_by_id("query").send_keys(u"毒app")
driver.find_element_by_id("stb").click()
time.sleep(3)
driver.quit()