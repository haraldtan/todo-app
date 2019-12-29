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

def test_access_LoginPage_Failed():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/login/')
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Page not found')]")
    
def test_access_RegisterPage():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    assert driver.find_element_by_name("username") and driver.find_element_by_name("password1") and driver.find_element_by_name("password2")

def test_access_RegisterPage_Failed():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/register/')
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Page not found')]")
    
def test_access_ToDoPage():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/todo/') 
    assert driver.find_element_by_xpath("//*[contains(text(), 'Login to view To-Do list')]") 

def test_access_ToDoPage_Failed():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/todolist/')
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Page not found')]")
    