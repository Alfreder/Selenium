# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
driver.get('https://huilansame.github.io')
l = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/p[2]/a[2]').text
print(l)

locator = (l, "CSDN")

try:
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(locator))
    print( driver.find_element_by_link_text('CSDN').get_attribute('href'))
finally:
    #time.sleep(10)
    driver.close()