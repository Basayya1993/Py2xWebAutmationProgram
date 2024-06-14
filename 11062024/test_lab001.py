import time

from selenium import webdriver


def test_web_open():
    driver = webdriver.Edge()
    driver.get("https://google.co.in")
    driver.maximize_window()

    time.sleep(10)
    driver.close()
    time.sleep(5)