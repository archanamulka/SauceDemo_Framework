# File description: This is the file with page class for "checkout Your information" page
# Page url: https://www.saucedemo.com/cart.html
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023


from features.Pages.base_page import BasePage


class YourCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    product_remove_bolt_tshirt_xpath = "//button[@id='remove-sauce-labs-bolt-t-shirt']"
    product_remove_labs_backpack_xpath = "//button[@id='remove-sauce-labs-backpack']"
    product_remove_labs_bike_xpath = "//button[@id='remove-sauce-labs-bike-light']"
    product_remove_labs_fleece_jacket_xpath = "//button[@id='remove-sauce-labs-fleece-jacket']"
    product_remove_lab_onesie_xpath = "//button[@id='remove-sauce-labs-onesie']"
    product_remove_test_xpath = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"

    checkout_id = "checkout"

    # below method takes product_name as argument and verifies if the item is present in the cart

    def verify_item_present_in_cart(self, product_name):

        if product_name == "Sauce Labs Backpack":
            assert self.is_element_displayed("product_remove_labs_backpack_xpath", self.product_remove_labs_backpack_xpath)

        elif product_name == "Sauce Labs Bike Light":
            assert self.is_element_displayed("product_remove_labs_bike_xpath", self.product_remove_labs_bike_xpath)
        
        elif product_name == "Sauce Labs Bolt T-shirt":
            assert self.is_element_displayed("product_remove_bolt_tshirt_xpath", self.product_remove_bolt_tshirt_xpath)

        elif product_name == "Sauce Labs Fleece Jacket":
            assert self.is_element_displayed("product_remove_labs_fleece_jacket_xpath", self.product_remove_labs_fleece_jacket_xpath)

        elif product_name == "Sauce Labs Onesie":
            assert self.is_element_displayed("product_remove_lab_onesie_xpath", self.product_remove_lab_onesie_xpath)

        elif product_name == "Red T-shirt":
            assert self.is_element_displayed("product_remove_test_xpath", self.product_remove_test_xpath)
    
    
    # below method clicks on checkout button

    def click_checkout(self):
        self.click_on_element("checkout_id", self.checkout_id)
    