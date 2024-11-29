from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

# 元素的定位
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

# 1 通过id定位
el1 = driver.find_element(By.ID,"kw")
el1.send_keys("Thw")
sleep(1)

# 2 通过 name 定位
el2 = driver.find_element(By.NAME,"wd")
el2.send_keys("YQT")
sleep(1)

# 3 通过 class name 类属性定位
el3=driver.find_element(By.CLASS_NAME,"s_ipt")
el3.send_keys("123")
sleep(1)

# 4 tag name 定位不到，因为页面太多一样的标签了 通常不用

# 定位超链接 a 标签的方式
# 5精准定位超链接文本信息
driver.find_element(By.LINK_TEXT,"百度首页").click()
sleep(1)
# 6模糊定位超链接文本信息
# driver.find_element(By.PARTIAL_LINK_TEXT,"hao").click()
# sleep(1)

# 7 通过css 定位 （用的少）
# 针对元素的属性：id,name,class name input
# id:#id
# name:[name=""]
# class_name = .class_name
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys(666)
sleep(1)


# 8 Xpath
# 可以解决 90% 以上的元素定位问题
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("XPATH")
sleep(1)


# 关闭驱动对象
driver.quit()