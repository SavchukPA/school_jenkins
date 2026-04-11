
import time
from selenium import webdriver

def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")

    time.sleep(5)

    assert "Python" in driver.title
    time.sleep(5)

    driver.quit()