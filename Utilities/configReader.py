# File description: This is the file that contains a method to read config file
# Author: Archana Mulka
# Created: 28/05/2023 
# Last modified: 28/05/2023

from configparser import ConfigParser

# below method takes category and key as arguments, reads the config file and returns the category and key values

def read_config_file(category, key):
    config = ConfigParser()                           # creating an object of ConfigParser class
    config.read("configurations/config.ini")          # reads the config file location
    return config.get(category, key)                  # returns category and key values


