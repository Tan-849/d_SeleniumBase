from argparse import Action
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

# 创建事件链对象
ac_chains = ActionChains(driver)

el1=driver.find_element(By.XPATH,'//*[@id="kw"]')
# 1 右击操作
ac_chains.context_click(el1)
ac_chains.perform()
sleep(1)


# 2 双击操作
el1.send_keys("123")
ac_chains.double_click(el1) #双击会全选
ac_chains.perform()
sleep(1)


# 3 悬停操作
driver.refresh()
el2=driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
ac_chains.move_to_element(el2)
ac_chains.perform()
sleep(1)


# 4 拖拽
driver.refresh()
sleep(1)
el3=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li[1]/a/span[2]')
ac_chains.drag_and_drop(el3,el1)
ac_chains.perform()
sleep(1)



# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()