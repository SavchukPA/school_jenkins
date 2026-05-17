import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page.home_page import HomePage
from pages.new_item_page import locators

# @pytest.mark.dependency(name="test_create_folder")
# def test_create_folder(browser):
#     ex_name_folder = "Test Folder"
#     element_is_clickable(browser, button_new_item_locator).click()
#     element_is_visible(driver=browser, locator=input_name_locator).send_keys(
#         ex_name_folder
#     )
#     element_is_visible(browser, list_folder_locator).click()
#     element_is_clickable(browser, button_submit_locator).click()
#     element_is_visible(browser, input_description).send_keys("Test Description")
#     element_is_clickable(browser, button_save).click()
#     browser.get("http://localhost:8080/")
#     time.sleep(2)
#     ac_name_folder = element_is_visible(driver=browser, locator=table_name_folder).text
#     assert (
#         ac_name_folder == ex_name_folder
#     ), f"Expected: {ex_name_folder}, Actual: {ac_name_folder}"


class NewItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(driver=driver)

    def click_new_item(self):
        self._element_is_clickable(locators.button_new_item_locator).click()

    def input_name_new_item(self, name):
        self._element_is_visible(locators.input_name_locator).send_keys(name)

    def set_folder_in_list_items(self):
        self._element_is_visible(locators.list_folder_locator).click()

    def set_folder_in_list_items_by_type(self, type_item: str):
        self._element_is_visible(
            locators.list_folder_locator_by_type(type=type_item)
        ).click()

    def click_submit_button(self):
        self._element_is_clickable(locators.button_submit_locator).click()

    def input_description(self, description: str):
        self._element_is_visible(locators.input_description).send_keys(description)
        time.sleep(1)

    def click_button_save(self):
        self._element_is_clickable(locators.button_save).click()

    def get_item_name(self):
        self._element_is_visible(locators.title_item)

    def create_item(self, name: str, description: str, type_item: str):
        self.click_new_item()
        self.input_name_new_item(name=name)
        self.set_folder_in_list_items_by_type(type_item=type_item)
        self.click_submit_button()
        self.input_description(description=description)
        self.click_button_save()

    def update_item(self, current_name):
        self.go_home_page()
        self.home_page.get_item_page_by_name(name=current_name)
