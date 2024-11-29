from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

el1=driver.find_element(By.XPATH,'//*[@id="kw"]')
el1.send_keys("123")
sleep(1)
# ctrl + A
el1.send_keys(Keys.CONTROL,"a")
sleep(1)
el1.send_keys(Keys.CONTROL,"c")
sleep(1)
el1.send_keys(Keys.BACKSPACE)
sleep(1)
el1.send_keys("456")
sleep(1)
el1.send_keys(Keys.CONTROL,"a")
sleep(1)
el1.send_keys(Keys.CONTROL,"v")
sleep(1)


# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()