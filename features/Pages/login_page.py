# File description: This is the file with page class for "Login" page
# Page url: https://www.saucedemo.com/
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from features.Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.Pages.products_page import ProductsPage

class loginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # Calling parent class constructor

    username_id = "user-name"
    password_id = "password"
    login_id = "login-button"
    
     

    def get_username(self):
        login_credentials = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']").text
        login_cred_list = login_credentials.split('\n')
        username = login_cred_list[1]
        return username
    
    def get_password(self):
        login_password = self.driver.find_element(By.XPATH, "//div[@class='login_password']").text
        login_password_list = login_password.split('\n')
        password = login_password_list[1]
        return password

    def enter_username(self):
        self.enter_input_into_element("username_id", self.username_id, self.get_username())

    def enter_password(self):
        self.enter_input_into_element("password_id", self.password_id, self.get_password())
    
    def click_login(self):
        self.click_on_element("login_id", self.login_id)
        return ProductsPage(self.driver)
       
    












