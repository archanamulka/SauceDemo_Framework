# File description: This is the file with parent class which has the most commonly used re-usable methods
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023

from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
     
    # below method determines the locator type and stores the locator in element 
    def find_element_type(self, locator_type, locator_value):

        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_classname"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_partiallinktext"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif locator_type.endswith("_tagname"):
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        elif locator_type.endswith("_cssselector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        return element
    
    def find_elements_type(self, locator_type, locator_value):

        if locator_type.endswith("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_type.endswith("_classname"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_partiallinktext"):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, locator_value)
        elif locator_type.endswith("_tagname"):
            elements = self.driver.find_elements(By.TAG_NAME, locator_value)
        elif locator_type.endswith("_cssselector"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        elif locator_type.endswith("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)

        return elements

    # below method clicks on given element and takes locator type and locator value as arguments
    def click_on_element(self, locator_type, locator_value):
        element = self.find_element_type(locator_type, locator_value)
        element.click()
    
    # below method clicks enters input into given element and takes locator type, locator value, input text as arguments
    def enter_input_into_element(self, locator_type, locator_value, input_text):
        element = self.find_element_type(locator_type, locator_value)
        element.send_keys(input_text)
    
    def is_element_displayed(self, locator_type, locator_value):
        element = self.find_element_type(locator_type, locator_value)
        return element.is_displayed()
    
    
