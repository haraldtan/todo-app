import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_access_LoginPage():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    assert driver.find_element_by_name("username") and driver.find_element_by_name("password")
    
def test_access_RegisterPage():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    assert driver.find_element_by_name("username") and driver.find_element_by_name("password1") and driver.find_element_by_name("password2")
    
def test_access_ToDoPage():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/todo/') 
    assert driver.find_element_by_xpath("//*[contains(text(), 'Login to view To-Do list')]")  