import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_InvalidUsername_ValidPassword():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    driver.find_element_by_name("username").send_keys("team")
    driver.find_element_by_name("password").send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Please enter a correct username and password. Note that both fields may be case-sensitive.')]")

def test_validUsername_InvalidPassword():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    driver.find_element_by_name("username").send_keys("team5")
    driver.find_element_by_name("password").send_keys("password")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Please enter a correct username and password. Note that both fields may be case-sensitive.')]")

def test_OnlyvalidUsername():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("team5")
    password.send_keys("")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = password.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_OnlyvalidPassword():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("")
    password.send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = username.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_NoCredentials():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("")
    password.send_keys("")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = username.get_attribute("validationMessage")
    message = password.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_validCredentials():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/login/')
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("team5")
    password.send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_name("logout-button")