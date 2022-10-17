import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
driver.execute_script('window.scrollBy(0,600);')
Selenium_Ruby_btn=driver.find_element_by_css_selector('.post-160 .woocommerce-LoopProduct-link h3').click()
time.sleep(3)
Reviews_btn=driver.find_element_by_css_selector('.reviews_tab').click()
Star_btn=driver.find_element_by_css_selector('.star-5').click()
Review_comment=driver.find_element_by_id('comment')
Review_comment.send_keys('Nice book!')
Name=driver.find_element_by_id('author')
Name.send_keys('XXX')
Mail=driver.find_element_by_id('email')
Mail.send_keys('mail@mail.com')
submit_btn=driver.find_element_by_css_selector('.submit')

driver.quit()

