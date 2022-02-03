# selenium的自动化操作
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)
search_input=driver.find_element_by_id('kw')
search_input.send_keys('周杰伦')
btn = driver.find_element_by_id('su')
btn.click()
time.sleep(3)
driver.back()
time.sleep(5)
driver.quit()