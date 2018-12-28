# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#返回列表
#driver.find_elements_by_xpath('//*[@class="mini-grid-row"]/td[3]/div')
def mySelenium():
    try:
        for i in range(2,1000):
            driver.find_element_by_xpath('//*[@id="mini-188"]/span/span').click()
            #driver.find_element_by_xpath('//*[@id="mini-182"]/div[1]/table/tbody/tr/td[1]/span[3]/input')
            time.sleep(10)
            data = driver.page_source
            time.sleep(2)
            with open(r'/Users/kun/Desktop/enterprises/write_data_'+str(i)+'.html', 'w') as f:
                f.write(data)
            time.sleep(2)
            f.close()
    except Exception as e:
        print(e)
        time.sleep(3600)
        driver.quit()
    finally:
        time.sleep(3600)
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = 'https://saas.elecredit.com/saas/embed/company_list/?sign=9d7941a28bf06c276e40b96e8289d56865be3b1c5c7391deaf29943fcfd5392a&adv=0'
    driver.get(url)
    time.sleep(60)
    mySelenium()
"""
input = driver.find_element_by_xpath('//*[@id="mini-182"]/div[1]/table/tbody/tr/td[1]/span[3]/input')
input.clear() 
input.send_keys('5')
from selenium.webdriver.common.keys import Keys
input.send_keys(Keys.ENTER)

"""