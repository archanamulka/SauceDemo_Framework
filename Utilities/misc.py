from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()



driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

product_names_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
product_descs_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item_desc']")
product_price_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
product_quantity_list = driver.find_elements(By.XPATH, "//div[@class='cart_quantity']")

def product_name(list):
    for product_name_ele in list:
        print(product_name_ele.text)

def product_desc(list):
    for product_desc_ele in list:
        print(product_desc_ele.text)
    
def product_price(list):
    for product_price_ele in list:
        print(product_price_ele.text)

def product_quantity(list):
    for product_quantity_ele in list:
        print(product_quantity_ele.text)

product_name(product_names_list)
product_desc(product_descs_list)
product_price(product_price_list)
product_quantity(product_quantity_list)

time.sleep(3)
driver.close()