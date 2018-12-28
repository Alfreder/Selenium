# -*- coding:utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
url = 'https://saas.elecredit.com/saas/embed/company_list/?sign=db1d313be69cfbf33870b79919479c72b7450d22b8888ab62204a36c44ec2be9&adv=0'
driver.get(url)
#driver.find_element_by_id('kw').clear()
#driver.find_element_by_id('kw').send_keys(str)
#driver.find_element_by_id('su').click()
data = driver.page_source
filename = 'data1.txt'
with open('write_data.txt', 'w+') as f:
    f.write(data)

while True:

    driver.find_element_by_xpath('//*[class="mini-grid-row]/td[3]/div').text

    l = driver.find_elements_by_xpath('//*[@id="datagrid_main"]/div/div[2]/div[4]/div[2]/div/table/tbody[@class="mini-grid-row"]')
    time.sleep(10)
    data = driver.page_source
    time.sleep(2)
    with open('write_data.txt', 'a+') as f:
        f.write(data)
    time.sleep(2)
    f.close()