import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import allure


def test_web_app_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()

    # <input type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # data-gtm-form-interact-field-id="0">

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("admin")

    time.sleep(10)
    # <input type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="1">

    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("password123")

    time.sleep(10)
    # <button type="submit" id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
    # <span class="icon loader hidden" data-qa="zuyezasugu"></span>
    # <span data-qa="ezazsuguuy">Sign in</span>
    # </button>

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    time.sleep(5)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
