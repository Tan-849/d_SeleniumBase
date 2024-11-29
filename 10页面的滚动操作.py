from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%9B%B4%E5%B8%8C%E6%9C%9B%E7%99%BE%E8%8A%B1%E9%BD%90%E6%94%BE&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1')

# 页面最大化
driver.maximize_window()

# 定义 js 脚本

js_str = "window.scrollTo(0,1000000)"
driver.execute_script(js_str)

sleep(1)
# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()