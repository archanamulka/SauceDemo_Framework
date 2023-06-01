# File description: This is the file with page class for "checkout overview" page
# Page url: https://www.saucedemo.com/checkout-step-two.html
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023

from features.Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutOverview(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)


    product_names_xpath = "//div[@class='inventory_item_name']"
    product_descs_xpath = "//div[@class='inventory_item_desc']"
    product_prices_xpath = "//div[@class='inventory_item_price']"
    product_quantities_xpath = "//div[@class='cart_quantity']"


    def verify_product_name(self, expected_product_name):
        product_name_list = self.find_elements_type("product_names_xpath", self.product_names_xpath)
        for product_name_ele in product_name_list:
            if product_name_ele.text == expected_product_name:
                assert True
            else:
                assert False, "Expected product not found on checkout page"
    
    def verify_product_desc(self, expected_product_desc):
        product_desc_list = self.find_elements_type("product_descs_xpath", self.product_descs_xpath)
        for product_desc_ele in product_desc_list:
            if product_desc_ele.text == expected_product_desc:
                assert True
            else:
                assert False, "Expected product desc not found on checkout page"

    def verify_product_price(self, expected_product_price):
        product_price_list = self.find_elements_type("product_prices_xpath", self.product_prices_xpath)
        for product_price_ele in product_price_list:
            if product_price_ele.text == expected_product_price:
                assert True
            else:
                assert False, "Expected product price not found on checkout page"

    def verify_product_quantity(self, expected_product_quantity):
        product_quantity_list = self.find_elements_type("product_quantities_xpath", self.product_quantities_xpath)
        for product_quantity_ele in product_quantity_list:
            if int(product_quantity_ele.text) == expected_product_quantity:
                assert True
            else:
                assert False, "Expected product quantity not found on checkout page"




    
