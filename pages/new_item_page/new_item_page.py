import time

from selenium.webdriver.common.by import By

from data.test_cases.new_item import ItemTypes
from pages.base_page import BasePage
from pages.home_page.home_page import HomePage
from pages.new_item_page import locators


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

    def set_item_in_list_items_by_type(self, item_type: ItemTypes):
        self._element_is_visible(
            locators.list_item_locator_by_type(item_type=item_type.value)
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

    def create_item(
        self,
        name: str | None = None,
        description: str | None = None,
        item_type: ItemTypes | None = None,
        data: dict | None = None,
    ) -> None:
        """
        Создание нового item
        Передать параметры: name, item_type
        Необязательный параметр: description
        Или передать словарь тест-кейс

        :param name: Имя
        :param description: Описание
        :param item_type: Enum item ItemTypes
        :param data: test case
        :return: None
        """

        if data:
            name = data["name"]
            description = data["description"]
            item_type = data["type"]
        self.click_new_item()
        self.input_name_new_item(name=name)
        self.set_item_in_list_items_by_type(item_type=item_type)
        self.click_submit_button()
        self.input_description(description=description)
        self.click_button_save()

    def update_item(self, current_name):
        self.go_home_page()
        self.home_page.get_item_page_by_name(name=current_name)
