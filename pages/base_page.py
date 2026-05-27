import os

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = os.environ.get("HOST")

    def go_home_page(self):
        from pages.home_page.home_page import HomePage

        self.driver.execute_script("""
            var logo = document.querySelector('.jenkins-mobile-hide');
            if (logo) logo.click();
        """)

        return HomePage(self.driver)

    def open(self, url):
        self.driver.get(url)

    def _element_is_visible(self, locator: tuple[str, str], timeout=10) -> WebElement:
        print(f"Поиск элемента: {locator}")
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def _elements_are_visible(
        self, locator: tuple[str, str], timeout=10
    ) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def _element_is_present(self, locator: tuple[str, str], timeout=10) -> WebElement:
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def _elements_are_present(
        self, locator: tuple[str, str], timeout=10
    ) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def _element_is_not_visible(self, locator: tuple[str, str], timeout=10):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def _element_is_clickable(self, locator: tuple[str, str], timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
