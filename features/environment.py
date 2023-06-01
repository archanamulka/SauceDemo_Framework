# File description: This is the file with behave hook steps (before_scenario, after_scenario, before_step, after_Step etc)
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 29/05/2023

from behave import *
import allure
from allure import attachment_type
from selenium import webdriver
from Utilities import configReader

def before_scenario(context, scenario):

    browser_name = configReader.read_config_file("url and browser", "browser")

    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    if browser_name == "firefox":
        context.driver = webdriver.Firefox()
    if browser_name == "edge":
        context.driver = webdriver.Edge()
    
    url = configReader.read_config_file("url and browser", "url")
    context.driver.get(url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


def after_scenario(context,scenario):
    context.driver.quit()


def after_step(context, step):
    allure.attach(context.driver.get_screenshot_as_png(), 
                      name='screenshot', 
                      attachment_type=attachment_type.PNG)
    

        

        
