# -*- coding:utf-8 -*-

from selenium import webdriver
import time

def mySelenium(t,str):
    try:
#        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver = webdriver.Safari()#executable_path="/usr/local/bin/geckodriver")

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys(str)
        driver.find_element_by_id('su').click()

    except Exception as e:
        print(e)
        driver.quit()
    finally:
        time.sleep(t)
        driver.quit()

if __name__ == "__main__":
    mySelenium(5,'你好')