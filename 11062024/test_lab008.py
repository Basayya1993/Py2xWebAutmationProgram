import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


def test_web_automation_positive_tc():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Initial-Page", attachment_type=AttachmentType.PNG)
    # https://www.idrive360.com/enterprise/account?upgradenow=true

    username_element = driver.find_element(By.XPATH, "//input[@id='username']")
    username_element.send_keys("augtest_040823@idrive.com")
    time.sleep(5)

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("123456")
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Login-Page", attachment_type=AttachmentType.PNG)

    # //button[@id='frm-btn']
    button_element = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    button_element.click()
    time.sleep(20)

    # //h5[@class='id-card-title']
    # <h5 _ngcontent-hrw-c10="" class="id-card-title">Your free trial has expired</h5>
    error_message_element = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")
    print(error_message_element)
    time.sleep(5)
    assert error_message_element.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="Error-Message", attachment_type=AttachmentType.PNG)

    time.sleep(5)
    driver.quit()
