# File description: This is the file with page class for "products" page
# Page url: https://www.saucedemo.com/inventory.html
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023


from features.Pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)            # Calling parent class constructor
    
    products_xpath = "//span[@class='title']"
    product_add_to_cart_bolt_tshirt_xpath = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    product_add_to_cart_labs_backpack_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_add_to_cart_labs_bike_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    product_add_to_cart_labs_fleece_jacket_xpath = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    product_add_to_cart_lab_onesie_xpath = "//button[@id='add-to-cart-sauce-labs-onesie']"
    product_add_to_cart_test_xpath = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    product_remove_bolt_tshirt_xpath = "//button[@id='remove-sauce-labs-bolt-t-shirt']"
    product_remove_labs_backpack_xpath = "//button[@id='remove-sauce-labs-backpack']"
    product_remove_labs_bike_xpath = "//button[@id='remove-sauce-labs-bike-light']"
    product_remove_labs_fleece_jacket_xpath = "//button[@id='remove-sauce-labs-fleece-jacket']"
    product_remove_lab_onesie_xpath = "//button[@id='remove-sauce-labs-onesie']"
    product_remove_test_xpath = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"

    cart_icon_xpath = "//span[@class='shopping_cart_badge']"

    sort_select_classname = "product_sort_container"


    def is_product_title_displayed(self):
        return self.is_element_displayed("products_xpath", self.products_xpath)
    
    
    def add_product_to_cart_and_verify(self, product_name):

        if product_name == "Sauce Labs Backpack":
            self.click_on_element("product_labs_backpack_xpath", self.product_add_to_cart_labs_backpack_xpath)
            assert self.is_element_displayed("product_remove_labs_backpack_xpath", self.product_remove_labs_backpack_xpath)

        elif product_name == "Sauce Labs Bike Light":
            self.click_on_element("product_labs_bike_xpath", self.product_add_to_cart_labs_bike_xpath)
            assert self.is_element_displayed("product_remove_labs_bike_xpath", self.product_remove_labs_bike_xpath)
        
        elif product_name == "Sauce Labs Bolt T-shirt":
            self.click_on_element("product_bolt_tshirt_xpath", self.product_add_to_cart_bolt_tshirt_xpath)
            assert self.is_element_displayed("product_remove_bolt_tshirt_xpath", self.product_remove_bolt_tshirt_xpath)

        elif product_name == "Sauce Labs Fleece Jacket":
            self.click_on_element("product_labs_fleece_jacket_xpath", self.product_add_to_cart_labs_fleece_jacket_xpath)
            assert self.is_element_displayed("product_remove_labs_fleece_jacket_xpath", self.product_remove_labs_fleece_jacket_xpath)

        elif product_name == "Sauce Labs Onesie":
            self.click_on_element("product_lab_onesie_xpath", self.product_add_to_cart_lab_onesie_xpath)
            assert self.is_element_displayed("product_remove_lab_onesie_xpath", self.product_remove_lab_onesie_xpath)

        elif product_name == "Red T-shirt":
            self.click_on_element("product_test_xpath", self.product_add_to_cart_test_xpath)
            assert self.is_element_displayed("product_remove_test_xpath", self.product_remove_test_xpath)

    def click_on_cart_icon(self):
        self.click_on_element("cart_icon_xpath", self.cart_icon_xpath)
    
    def sort_products(self, sort_type):
        select = Select(self.find_element_type("sort_select_classname", self.sort_select_classname))

        if sort_type == "atoz":
            select.select_by_visible_text("Name (A to Z)")

        if sort_type == "ztoa":
            select.select_by_visible_text("Name (Z to A)")

        if sort_type == "lotohi":
            select.select_by_visible_text("Price (low to high)")
            
        if sort_type == "hitolo":
             select.select_by_visible_text("Price (high to low)")
            
        
             




