from selenium.webdriver.common.by import By

title_item_in_table = lambda title: (
    By.XPATH,
    f"//td//span[contains(text(), '{title}')]",
)
description = (By.XPATH, "//div[@id='view-message']")
description_content = (By.XPATH, "//div[@id='description-content']")
title = (By.XPATH, "//h1")
left_menu_button_rename = (By.XPATH, "//a[contains(@href, 'confirm-rename')]")
input_new_name = (By.XPATH, "//input[@name='newName']")
button_rename = (By.XPATH, "//button[@value='Rename']")
left_menu_button_delete = (By.XPATH, "//a[@data-title='Delete Folder']")
button_confirm_delete = (By.XPATH, "//button[@data-id='ok']")
