from selenium import webdriver


def web_test_browser():
    driver = webdriver.Edge()

    driver.back()
    driver.forward()
    driver.refresh()
    
