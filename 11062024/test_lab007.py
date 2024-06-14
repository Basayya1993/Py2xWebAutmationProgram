import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from faker import Faker

faker = Faker()


def test_web_app_positive_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Initial-Page", attachment_type=AttachmentType.PNG)

    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()

    time.sleep(5)
    # <input
    # type="text"
    # class="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value=""
    # autocomplete="off"
    # >
    username_appointment = driver.find_element(By.ID, "txt-username")
    username_appointment.send_keys(faker.user_name())
    time.sleep(5)
    # <input
    # type="password"
    # class="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value=""
    # autocomplete="off"
    # >
    password_appointment = driver.find_element(By.ID, "txt-password")
    password_appointment.send_keys(faker.password())
    time.sleep(10)
    # <button
    # id="btn-login"
    # type="submit"
    # class="btn
    # btn-default"
    # Login</button>
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    login_appointment = driver.find_element(By.ID, "btn-login")
    login_appointment.click()
    time.sleep(5)
    # <p
    # class="lead text-danger"
    # >Login failed! Please ensure the username and password are valid.
    # </p>
    # //p[@class='lead text-danger']
    time.sleep(5)
    error_msg_appointment = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    time.sleep(5)
    print(error_msg_appointment)
    time.sleep(5)
    assert error_msg_appointment.text == "Login failed! Please ensure the username and password are valid."
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Error-Message", attachment_type=AttachmentType.PNG)

    time.sleep(5)

    driver.quit()
