import time
import allure
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


def test_web_app_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    time.sleep(5)

    # Use //a[@id='btn-make-appointment']
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg"
    # >Make Appointment
    # </a>

    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    time.sleep(5)

    driver.quit()
