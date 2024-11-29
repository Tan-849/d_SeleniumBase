from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('http://localhost:63342/d_WebTest/day01/select.html?_ijt=fibhmmv2u6f1tk6l1djcdsqdle&_ij_reload=RELOAD_ON_SAVE')

# 页面最大化
driver.maximize_window()


select=Select(driver.find_element(By.XPATH, '//*[@id="cars"]'))
# ○ 通过索引选择定位
select.select_by_index(2) # 吉利
sleep(2)
# ○ 通过文本内容选择定位
select.select_by_visible_text("比亚迪")
sleep(2)
# ○ 通过属性value选择定位
select.select_by_value("volvo") #沃尔沃
sleep(2)


# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()