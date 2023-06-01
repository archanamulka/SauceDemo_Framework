# File description: This is the step definition file for the BDD test scenarios in checkout.feature file
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 30/05/2023


from behave import *
from features.Pages.checkout_overview_page import CheckoutOverview
from features.Pages.checkout_your_info_page import CheckoutYourInfo
from features.Pages.login_page import loginPage
from features.Pages.products_page import ProductsPage
from features.Pages.your_cart_page import YourCartPage
import time


@given(u'user is logged into Sauce Demo website')
def login_to_sauce_demo(context):

    context.login_page = loginPage(context.driver)
    context.login_page.enter_username()
    context.login_page.enter_password()
    context.products_page = context.login_page.click_login()
   
    assert context.products_page.is_product_title_displayed()

@when(u'user sorts the products by Price - low to high')
def sort_products_price_low_to_high(context):
    context.products_page.sort_products("lotohi")
    time.sleep(2)

@when(u'adds the product "{productname}" to cart')
def add_bolt_tshirt_to_cart(context, productname):
    
    context.products_page.add_product_to_cart_and_verify("Sauce Labs Bolt T-shirt")
    context.products_page.click_on_cart_icon()
                                                          
    context.your_cart_page = YourCartPage(context.driver)
    context.your_cart_page.verify_item_present_in_cart(productname)
    context.your_cart_page.click_checkout()

@when('continues to checkout by entering first name as "{firstname}", last name as "{lastname}" and postal code as "{postcode}"')
def enter_firstname_lastname_postalcode_and_continue(context, firstname, lastname, postcode):
    context.checkout_one_page = CheckoutYourInfo(context.driver)
    context.checkout_one_page.enter_first_name(firstname)
    context.checkout_one_page.enter_last_name(lastname)
    context.checkout_one_page.enter_postal_code(postcode)
    time.sleep(2)
    context.checkout_one_page.click_continue()


@then('the below product details on checkout overview page are displayed correctly')
def verify_checkout_details(context):
    checkout_two_page = CheckoutOverview(context.driver)

    for row in context.table:
        checkout_two_page.verify_product_name(row["name"])
        checkout_two_page.verify_product_desc(row["desc"])
        checkout_two_page.verify_product_price(row["price"])
        checkout_two_page.verify_product_quantity(int(row["quantity"]))

    


 


