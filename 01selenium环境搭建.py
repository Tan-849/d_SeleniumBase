from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()