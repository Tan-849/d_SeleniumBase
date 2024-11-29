from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')


# ● 浏览器的最大化
driver.maximize_window()
sleep(1)

# ● 设置浏览器的分辨率（宽高）
driver.set_window_size(600,600)
sleep(1)

# ● 设置浏览器的相对位置
driver.set_window_position(100,600)
sleep(1)

# ● 浏览器的刷新操作
driver.refresh()
sleep(1)

# ● 浏览器的前进
# ● 浏览器的回退
el2 = driver.find_element(By.XPATH,'//*[@id="kw"]')
el3 = driver.find_element(By.XPATH,'//*[@id="su"]')
driver.maximize_window()

el2.send_keys("123")
sleep(1)
el3.click()
sleep(1)
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(1)

print(driver.title)
print(driver.current_url)



# ● 关闭整个浏览器页面
driver.quit()

# ● 关闭浏览器的当前页面
driver.close()



# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()