#1111111111111111111111111111
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn=driver.find_element_by_link_text('My Account').click()
# Mail=driver.find_element_by_id('reg_email')
# Mail.send_keys('mail070@mail.com')
# Password=driver.find_element_by_id('reg_password')
# Password.send_keys('QWE123qwe!@#')
# Register_btn=driver.find_element_by_css_selector('[name="register"]').click()
#
# time.sleep(3)
#
# driver.quit()
#
#22222222222222222222222222222

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
my_acc_btn=driver.find_element_by_link_text('My Account').click()
Mail_login=driver.find_element_by_id('username')
Mail_login.send_keys('mail070@mail.com')
Password_login=driver.find_element_by_id('password')
Password_login.send_keys('QWE123qwe!@#')
Login_btn=driver.find_element_by_css_selector('[name="login"]').click()
time.sleep(5)

Logout_btn=driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation")
Logout_btn_text=Logout_btn.text
assert "Logout" in Logout_btn_text

driver.quit()