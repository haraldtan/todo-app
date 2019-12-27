import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_ExistingUser():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team5")
    driver.find_element_by_name("password1").send_keys("Password123")
    driver.find_element_by_name("password2").send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'A user with that username already exists.')]")

def test_Valid_150_Charcaters():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("Team5isatngeeannpolytechnic123456789008uyhtgfdcxvbnmefdsrht56rt24ghrwgh8wgh5thj5t8j589hathpe57hwor9aoghbvr89wthfeviFn4w085735trg4hqgnRWUgfgf7efehf8ehf")
    driver.find_element_by_name("password1").send_keys("Pass123word")
    driver.find_element_by_name("password2").send_keys("Pass123word")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.current_url == 'http://127.0.0.1:8000/accounts/login/'

def test_password_lessthan8Char():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    driver.find_element_by_name("password1").send_keys("Passwor")
    driver.find_element_by_name("password2").send_keys("Passwor")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'This password is too short. It must contain at least 8 characters.')]")

def test_password_allnumeric():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    driver.find_element_by_name("password1").send_keys("12345678")
    driver.find_element_by_name("password2").send_keys("12345678")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'This password is entirely numeric.')]")

def test_empty_username():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    username = driver.find_element_by_name("username")
    username.send_keys("")
    driver.find_element_by_name("password1").send_keys("Pass123word")
    driver.find_element_by_name("password2").send_keys("Pass123word")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = username.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_empty_password():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    password = driver.find_element_by_name("password1")
    password.send_keys("")
    driver.find_element_by_name("password2").send_keys("")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = password.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_notMatchingPassword():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    driver.find_element_by_name("password1").send_keys("Password12345")
    driver.find_element_by_name("password2").send_keys("Password123")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), \"The two password fields didn't match.\")]")
    
def test_empty_CfrmPassword():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    driver.find_element_by_name("password1").send_keys("Pass123word")
    password = driver.find_element_by_name("password2")
    password.send_keys("")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    message = password.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_ValidSignup():
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/accounts/register/')
    driver.find_element_by_name("username").send_keys("team52")
    driver.find_element_by_name("password1").send_keys("Pass123word")
    driver.find_element_by_name("password2").send_keys("Pass123word")
    submit = driver.find_element_by_name("submit")
    submit.click()
    time.sleep(0.5)
    assert driver.current_url == 'http://127.0.0.1:8000/accounts/login/'
