from selenium import webdriver
import time

login = ''
chromedriver = "/Users/dmitrijsazin/Desktop/test_task/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://passport.yandex.ru/auth/")
driver.find_element_by_xpath('//*[@id="passp-field-login"]').send_keys(login)
driver.find_element_by_xpath('//*[@id="passp:sign-in"]').click()
time.sleep(10)
driver.close()
driver.quit()


