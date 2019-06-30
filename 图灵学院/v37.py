from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
url = 'http://www.baidu.com'
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')

driver.get(url)

text = driver.find_element_by_id('wrapper').text

print(text)

#得到页面快照
driver.save_screenshot('index.png')

#id='kw'是百度的输入框，我们得到输入框的ui元素搜索‘大熊猫’
driver.find_element_by_id('kw').send_keys(u'大熊猫')

#id='su'是百度搜索框的按钮，click点击
driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot('daxiogmao.png')

#获取当前页的cookie
print(driver.get_cookies())

#模拟输入两个按键Ctrl+a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

#Ctrl+x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('hangmu.png')
#模拟回车
driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('hangmu2.png')
#清空输入框，clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#退出浏览器
driver.quit()