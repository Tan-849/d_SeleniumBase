from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
#导入显示等待的模块及包
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("fjklajkld")
driver.find_element(By.XPATH, '//*[@id="su"]').click()
# 不添加等待会报错
# 1 强制等待
# sleep(2)
# driver.find_element(By.XPATH, '//*[@id="1"]/div/div[1]/h3/a').click()

# 2 显式等待 （元素出现了就点）
# el1 = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]/div/div[1]/h3/a')))
# el1.click()

# 3 隐式等待
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="1"]/div/div[1]/h3/a').click()



# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()