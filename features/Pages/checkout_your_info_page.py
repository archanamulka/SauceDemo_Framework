# File description: This is the file with page class for "checkout Your information" page
# Page url: https://www.saucedemo.com/checkout-step-one.html
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023

from features.Pages.base_page import BasePage


class CheckoutYourInfo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_id = "first-name"
    last_name_id = "last-name"
    postal_code_id = "postal-code"
    continue_id = "continue"

    # input methods for entering first name, last name and postal code

    def enter_first_name(self, firstname):
        self.enter_input_into_element("first_name_id", self.first_name_id, firstname)
    
    def enter_last_name(self, lastname):
        self.enter_input_into_element("last_name_id", self.last_name_id, lastname)   

    def enter_postal_code(self, postalcode):
        self.enter_input_into_element("postal_code_id", self.postal_code_id, postalcode) 
    
    # below method clicks on continue button
    
    def click_continue(self):
        self.click_on_element("continue_id", self.continue_id)