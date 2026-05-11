from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pages


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)

    def jenkins_logo_click(self):
        for i in range(2):
            try:
                self.wait10.until(EC.element_to_be_clickable((By.CLASS_NAME, "app-jenkins-logo"))).click()
                break
            except StaleElementReferenceException:
                pass

        return pages.home_page.HomePage(self.driver)
