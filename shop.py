# 1111111111111111111111111111111
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn=driver.find_element_by_link_text('My Account').click()
# Mail_login=driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login=driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(5)
# Shop_btn=driver.find_element_by_link_text('Shop').click()
# time.sleep(5)
# HTML5_Forms=driver.find_element_by_css_selector('.post-181 .button.product_type_simple.ajax_add_to_cart').click()
# HTML5_Forms_h1=driver.find_element_by_tag_name('h1')
# HTML5_Forms_h1_text=HTML5_Forms_h1.text
# if HTML5_Forms_h1.text=='HTML5 Forms':
#     print('Правильный заголовок')
# else:
#     print('Не правильный заголовок')
#
# driver.quit()

# 222222222222222222222222222222222222222

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn=driver.find_element_by_link_text('My Account').click()
# Mail_login=driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login=driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(3)
# Shop_btn=driver.find_element_by_link_text('Shop').click()
# time.sleep(3)
# HTML_btn=driver.find_element_by_css_selector('.cat-item.cat-item-19>[href]').click()
# time.sleep(3)
# product = driver.find_elements_by_css_selector(".type-product")
# total_product=len(product)
# print('На странице показаны ' + str(total_product) + ' товара')
#
#
# driver.quit()

# 33333333333333333333333333333333

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn=driver.find_element_by_link_text('My Account').click()
# Mail_login=driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login=driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn=driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(3)
# Shop_btn=driver.find_element_by_link_text('Shop').click()
# time.sleep(3)
# default_btn=driver.find_element_by_css_selector('[value="menu_order"]')
# default_btn_text = default_btn.text
# print('В селекторе выбран вариант сортировки товаров: ' + str(default_btn_text) )
# select_btn=driver.find_element_by_css_selector('[name="orderby"].orderby')
# element=Select(select_btn)
# element.select_by_visible_text('Sort by price: high to low')
# time.sleep(5)
# default_btn2=driver.find_element_by_css_selector('[selected="selected"]')
# default_btn2_text = default_btn2.text
# print('В селекторе выбран вариант сортировки товаров: ' + str(default_btn2_text) )
#
# driver.quit()

# 44444444444444444444444444444444444

# import time
# from telnetlib import EC
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn = driver.find_element_by_link_text('My Account').click()
# Mail_login = driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login = driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn = driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(3)
# Shop_btn = driver.find_element_by_link_text('Shop').click()
# time.sleep(3)
# android_book = driver.find_element_by_css_selector('[data-product_id="169"]').click()
# time.sleep(3)
# old_price = driver.find_element_by_tag_name('del')
# old_price_text = old_price.text
# assert "600.00" in old_price_text
# new_price = driver.find_element_by_css_selector('ins .woocommerce-Price-amount.amount')
# new_price_text = new_price.text
# assert "450.00" in new_price_text
#
# android_logo = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.attachment-shop_single.size-shop_single.wp-post-image')))
# android_logo.click()
# android_close = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
# android_close.click()
#
# driver.quit()

# 555555555555555555555555555555555555

import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn = driver.find_element_by_link_text('My Account').click()
# Mail_login = driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login = driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn = driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(3)
# Shop_btn = driver.find_element_by_link_text('Shop').click()
# time.sleep(3)
# html_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# # pay1 = driver.find_element_by_css_selector('.cartcontents')
# # pay1_text = pay1.text
# # assert "1 item" in pay1_text
# pay2 = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
# pay2_text = pay2.text
# # assert "₹180.00" in pay2_text
# pay3 = driver.find_element_by_css_selector('.wpmenucart-contents').click()
# time.sleep(3)
# Subtotal=driver.find_element_by_css_selector('[data-title="Subtotal"] .woocommerce-Price-amount.amount')
# Subtotal_text=Subtotal.text
# assert Subtotal_text==pay2_text
# total=driver.find_element_by_css_selector('.order-total .woocommerce-Price-amount.amount')
# total_text=total.text
# print('Стоимость товаров: '+str(Subtotal_text) +'\n'+ 'Общая стоимость: '+ str(total_text))
# assert Subtotal_text != total_text
# driver.quit()

#6666666666666666666666666666666
#
# import time
# from telnetlib import EC
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_acc_btn = driver.find_element_by_link_text('My Account').click()
# Mail_login = driver.find_element_by_id('username')
# Mail_login.send_keys('mail070@mail.com')
# Password_login = driver.find_element_by_id('password')
# Password_login.send_keys('QWE123qwe!@#')
# Login_btn = driver.find_element_by_css_selector('[name="login"]').click()
# time.sleep(3)
# Shop_btn = driver.find_element_by_link_text('Shop').click()
# time.sleep(3)
# driver.execute_script('window.scrollBy(0,300);')
# html_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(5)
# js_data_book=driver.find_element_by_css_selector('[data-product_id="180"]').click()
# time.sleep(2)
# pay = driver.find_element_by_css_selector('.wpmenucart-contents').click()
# time.sleep(5)
# del_1=driver.find_element_by_css_selector('[data-product_id="182"]').click()
# undo_1=driver.find_element_by_css_selector('.woocommerce-message [href]').click()
# time.sleep(2)
# js_data_book_3=driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# js_data_book_3.clear()
# js_data_book_3.send_keys(3)
# time.sleep(3)
# upd_btn=driver.find_element_by_css_selector('[name="update_cart"]').click()
# time.sleep(3)
# apply_coupon=driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# time.sleep(3)
# error=driver.find_element_by_css_selector('.woocommerce-error')
# error_text=error.text
# assert error_text=='Please enter a coupon code.'
# driver.quit()

#777777777777777777777777777777777

import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_acc_btn = driver.find_element_by_link_text('My Account').click()
Mail_login = driver.find_element_by_id('username')
Mail_login.send_keys('mail070@mail.com')
Password_login = driver.find_element_by_id('password')
Password_login.send_keys('QWE123qwe!@#')
Login_btn = driver.find_element_by_css_selector('[name="login"]').click()
time.sleep(3)
Shop_btn = driver.find_element_by_link_text('Shop').click()
time.sleep(3)
driver.execute_script('window.scrollBy(0,300);')
html_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
pay = driver.find_element_by_css_selector('.wpmenucart-contents').click()
Proceed_to_Checkout_btn=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout [href]')))
Proceed_to_Checkout_btn.click()
name1=driver.find_element_by_id('billing_first_name')
name1.clear()
name1.send_keys('XXX')
name2=driver.find_element_by_id('billing_last_name')
name2.clear()
name2.send_keys('YYY')
phone=driver.find_element_by_id('billing_phone')
phone.clear()
phone.send_keys('123123123')
country=driver.find_element_by_id('s2id_billing_country').click()
country_rus=driver.find_element_by_css_selector('[role="combobox"]')
country_rus.send_keys('russia')
country_rus2=driver.find_element_by_css_selector('.select2-result-label').click()
Address=driver.find_element_by_css_selector('[placeholder="Street address"]')
Address.clear()
Address.send_keys('street')
city=driver.find_element_by_css_selector('[name="billing_city"]')
city.clear()
city.send_keys('Tomsk')
state=driver.find_element_by_css_selector('[name="billing_state"]')
state.clear()
state.send_keys('qwer')
Postcode=driver.find_element_by_css_selector('.validate-postcode .input-text')
Postcode.clear()
Postcode.send_keys('634000')
time.sleep(2)
driver.execute_script('window.scrollBy(0,600);')
time.sleep(2)
check=driver.find_element_by_css_selector('[value="cheque"]').click()
place_order_btn=driver.find_element_by_id('place_order').click()
time.sleep(5)
text1=driver.find_element_by_css_selector('.woocommerce-thankyou-order-received')
text1_text=text1.text
assert text1_text=='Thank you. Your order has been received.'
text2=driver.find_element_by_tag_name('tr:nth-child(3)>td')
text2_text=text2.text
assert text2_text=='Check Payments'

driver.quit()

