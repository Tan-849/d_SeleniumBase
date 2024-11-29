from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.jd.com')

# 页面最大化
driver.maximize_window()
driver.implicitly_wait(3)

# 页面切换
# ● 获取当前浏览器的所有页面信息
# 查看当前页面
print(driver.current_window_handle)
# 返回一个列表，列表中每个元素代表一个独立页面
print(driver.window_handles)


# 点击拍拍二手
driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[1]/div[2]/div[1]/div/div/ul/li[6]/a').click()
driver.switch_to.window(driver.window_handles[1])
# ● 获取单个页面信息
print(driver.current_window_handle)
# 查看所有页面
print(driver.window_handles)


# 点击电脑
driver.find_element(By.XPATH,'//*[@id="J_babelOptPage"]/div/div[2]/div/div/div[3]').click()
sleep(2)
driver.switch_to.window(driver.window_handles[2])
# 获取单个页面信息
print(driver.current_window_handle)
# 查看所有页面
print(driver.window_handles)



# 点击超市
driver.find_element(By.XPATH,'//*[@id="nav-chaoshi"]/a').click()
sleep(2)
driver.switch_to.window(driver.window_handles[3])
# ● 获取单个页面信息
print(driver.current_window_handle)
# 查看所有页面
print(driver.window_handles)


# ● 创建新的页面


# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()