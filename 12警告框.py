from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()

# 通过驱动对象访问被测页面
driver.get('http://localhost:63342/d_WebTest/day01/register.html?_ijt=dnu9f6lq1gton52g4sgf5s16jk&_ij_reload=RELOAD_ON_SAVE')

# 页面最大化
driver.maximize_window()

# 定义 js 脚本
js_str = "window.scrollTo(0,1000000)"
driver.execute_script(js_str)
sleep(1)

# 处理警告框
# 1 获取警告框元素
driver.find_element(By.XPATH, '//*[@id="alerta"]').click()
sleep(1)

# 2 切入警告框
alert1= driver.switch_to.alert
sleep(1)

# 3 获取警告框的元素
print(alert1.text)
sleep(1)

# 4 关闭警告框
# 4.1 确定按钮
# alert1.dismiss()
# sleep(1)

# 4.2 取消按钮
alert1.accept()
sleep(1)

# 5 针对需要输入内容的警告框，可以使用send_keys() 方法进行输入
# alert1.send_keys("123456")



# 等待 1s
sleep(1)
# 关闭驱动对象
driver.quit()