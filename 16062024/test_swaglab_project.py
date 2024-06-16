# Swag Labs web automation project for demo
# Ex: Input username :standard_user, locked_out_user, problem_user
# password :secret_sauce
# url : https://www.saucedemo.com/

import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


def test_web_swag_lab_automation():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    time.sleep(10)
    allure.attach(driver.get_screenshot_as_png(), name="Initial-Page", attachment_type=AttachmentType.PNG)

    username_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username_element.send_keys("standard_user")
    time.sleep(5)

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("secret_sauce")
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="login-Page", attachment_type=AttachmentType.PNG)

    # //input[@id='login-button']
    login_button_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button_element.click()
    time.sleep(5)

    add_cart_element = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_cart_element.click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="adding-item", attachment_type=AttachmentType.PNG)

    verify_cart_element = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
    verify_cart_element.click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Varify_Cart-Page", attachment_type=AttachmentType.PNG)

    checkout_element = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_element.click()
    time.sleep(5)

    information_firstname_element = driver.find_element(By.XPATH, "//input[@id='first-name']")
    information_firstname_element.send_keys("Abhishek")
    time.sleep(5)

    information_lastname_element = driver.find_element(By.XPATH, "//input[@id='last-name']")
    information_lastname_element.send_keys("Belagavi")
    time.sleep(5)

    information_zipcode_element = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    information_zipcode_element.send_keys("560123")
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Your-Information", attachment_type=AttachmentType.PNG)

    continue_element = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_element.click()
    time.sleep(5)

    finish_element = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_element.click()
    time.sleep(5)

    ordered_element = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
    print(ordered_element)
    # <h2 class="complete-header" data-test="complete-header">Thank you for your order!</h2>

    assert ordered_element.text == "Thank you for your order!"
    allure.attach(driver.get_screenshot_as_png(), name="Final-Page", attachment_type=AttachmentType.PNG)

    time.sleep(10)
    driver.quit()
