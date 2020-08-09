user_id='your_email@gmail.com'
password='your_password'

from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\\viral\\Desktop\\ISB\\day 2\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.facebook.com/')
ep=browser.find_element_by_id('email')
ep.send_keys(user_id)

pw=browser.find_element_by_id('pass')
pw.send_keys(password)

login=browser.find_element_by_id('u_0_b')
login.click()
