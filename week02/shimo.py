from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im')
    time.sleep(1)


    browser.find_element_by_xpath('//div[@class="entries"]/a[2]/button').click()
    time.sleep(5)

    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('13851633822')
    time.sleep(1)
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('********')

    browser.find_element_by_xpath('//button[contains(@class,"sm-button")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()