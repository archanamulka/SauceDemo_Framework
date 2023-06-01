# File description: This is the feature file which contains test cases in BDD format for checkout functionality on SauceDemo website
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 30/05/2023

Feature: Verify the checkout functionality on Sauce demo website


Scenario: Verify the checkout overview page displays the correct details when a user orders 'Sauce Labs Bolt T-Shirt'
    Given user is logged into Sauce Demo website
    When user sorts the products by Price - low to high
    And adds the product "Sauce Labs Bolt T-Shirt" to cart
    And continues to checkout by entering first name as "TestFN", last name as "TestLN" and postal code as "IG1 2BX"
    Then the below product details on checkout overview page are displayed correctly
        |name|desc|quantity|price|
        |Sauce Labs Bolt T-Shirt|Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.|1|$15.99|
    

