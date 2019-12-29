import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_noLogin_todo():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/todo/")
    assert driver.find_element_by_xpath("//*[contains(text(), 'Login to view To-Do list')]")

def test_login_todo():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/accounts/login/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("team5")
    password.send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_name("content") and driver.find_element_by_name("Add")
    