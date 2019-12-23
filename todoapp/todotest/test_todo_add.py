import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_add_InValid_ToDo_Object():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/accounts/login/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("team5")
    password.send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    driver.get("http://127.0.0.1:8000/todo/")
    todoobject = driver.find_element_by_name("content")
    todoobject.send_keys("Test1")
    submit = driver.find_element_by_name("Add")
    submit.click()
    assert driver.find_element_by_xpath("//*[contains(text(), 'Test1')]")

def test_addInValidToDoObject():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/accounts/login/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("team5")
    password.send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    driver.get("http://127.0.0.1:8000/todo/")
    todoobject = driver.find_element_by_name("content")
    submit = driver.find_element_by_name("Add")
    submit.click()
    message = todoobject.get_attribute("validationMessage")
    assert message == "Please fill out this field."