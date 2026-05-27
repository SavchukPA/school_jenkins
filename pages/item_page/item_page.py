import pages
from pages.base_page import BasePage
from pages.home_page.home_page import HomePage
from pages.item_page import locators
from data.test_cases.new_item import ItemTypes


class ItemPage(BasePage):

    def __init__(self, driver, name: str | None = None):
        super().__init__(driver)
        self.home_page = HomePage(driver)
        if name:
            self.home_page.get_item_page_by_name(name=name)

    def get_item_description_1(
        self,
    ) -> str:
        return self._element_is_visible(locator=locators.description).text

    def get_item_description_2(
        self,
    ) -> str:
        return self._element_is_visible(locator=locators.description_content).text

    def get_item_description(self, item_type: ItemTypes):
        match item_type:
            case (
                ItemTypes.PIPELINE
                | ItemTypes.FREESTYLE_PROJECT
                | ItemTypes.MULTI_CONFIGURATION_PROJECT
            ):
                return self.get_item_description_2()

            case (
                ItemTypes.FOLDER
                | ItemTypes.MULTIBRANCH_PIPELINE
                | ItemTypes.ORGANIZATION_FOLDER
            ):
                return self.get_item_description_1()

            case _:
                raise ValueError(f"Неправильный тип item: {item_type}")

    def get_item_name(self):
        return self._element_is_visible(locator=locators.title).text

    def click_rename_item_left_menu(self):
        self._element_is_visible(locator=locators.left_menu_button_rename).click()

    def input_new_name(self, new_name: str):
        self._element_is_visible(locator=locators.input_new_name).clear()
        self._element_is_visible(locator=locators.input_new_name).send_keys(new_name)

    def click_rename_button(self):
        self._element_is_clickable(locator=locators.button_rename).click()

    def click_delete_button_left_menu(self):
        self._element_is_visible(locator=locators.left_menu_button_delete).click()

    def click_confirm_delete(self):
        self._element_is_clickable(locator=locators.button_confirm_delete).click()

    def update_item(self, new_name):
        self.click_rename_item_left_menu()
        self.input_new_name(new_name)
        self.click_rename_button()

    def delete_item(self):
        self.click_delete_button_left_menu()
        self.click_confirm_delete()
