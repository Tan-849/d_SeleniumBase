from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

# 给页面设置 cookie 信息
driver.add_cookie({"name":"BIDUPSID","value":"95FA9083EAED5245ABF0455CEAA869BF"})
driver.add_cookie({"name":"BDUSS","value":"ktbU9tVlc3eFkxYy1-QXNVZmdXNXpJSWlINjh1M2VnZFZPbVhxUks5a1lUeGRuSVFBQUFBJCQAAAAAAAAAAAEAAABdrhc3dGh3xOOywr-pAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABjC72YYwu9mWH"})

# 清除页面缓存，一定要执行刷新操作
sleep(2)
driver.refresh()

# 等待 1s
sleep(5)
# 关闭驱动对象
driver.quit()