from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pages


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)

    def jenkins_logo_click(self):
        self.driver.find_element(By.CLASS_NAME, "app-jenkins-logo").click()

        return pages.home_page.HomePage(self.driver)
