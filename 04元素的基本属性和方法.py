from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('https://www.baidu.com')

# 页面最大化
driver.maximize_window()


el1= driver.find_element(by=By.XPATH, value='//*[@id="csaitab"]')

# ● 获取元素的大小（宽高）：size
print(el1.size)

# ● 获取元素的文本内容（如果该元素没有文本内容那么返回值是空值：text
print(el1.text)

# ● 获取元素的具体某个属性：get_attribute() 当不存在该属性时，返回空值
print(el1.get_attribute('class'))

# ● 查看元素是否可见（返回布尔值）：is_display()
print(el1.is_displayed())

# ● 查看元素是否可用（返回布尔值）：is_enable()
print(el1.is_enabled())



# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()