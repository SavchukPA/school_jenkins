from selenium.webdriver.common.by import By

from pages.base_page import BasePage

button_new_item_locator = (By.XPATH, '//a[contains(., "New Item")]')
input_name_locator = (By.XPATH, "//input[@id='name']")
list_folder_locator = (By.XPATH, "//li//span[text()='Folder']")
list_item_locator_by_type = lambda item_type: (
    By.XPATH,
    f"//li//span[text()='{item_type}']",
)
button_submit_locator = (By.XPATH, "//button[@type='submit']")
input_description = (By.XPATH, "//textarea[@class='jenkins-input   ']")
button_save = (By.XPATH, "//button[@value='Save']")
name_folder = (By.XPATH, "//h1[contains(text(), 'Test Folder')]")
description_folder = (By.XPATH, "//div[contains(text(), 'Test Description')]")
table_name_folder = (By.XPATH, "//tbody//td[3]")
error_message = (By.XPATH, "//div[@id='itemname-invalid']")
# button_rename = (By.XPATH, "//span[contains(text(), 'Rename')]")
# title_item_in_table = lambda title_item: (
#     By.XPATH,
#     f"//a/span[contains(text(), {title_item})]",
# )
title_item_in_table = (By.XPATH, "//a/span[contains(text(), 'Test Folder')]")
button_rename = (By.XPATH, "//a[contains(@href, 'confirm-rename')]")
input_new_name = (By.XPATH, "//input[@name='newName']")
button_submit = (By.XPATH, "//button[@name='Submit']")

title_item = (By.XPATH, "//h1")
