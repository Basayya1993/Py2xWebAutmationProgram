import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_app():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # <a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg"
    # >Make Appointment
    # </a>
    element = driver.find_element(By.ID,"btn-make-appointment")
    element.click()

    time.sleep(20)
    driver.quit()

