from selenium.webdriver.common.by import By

name_item_in_table = lambda name: (
    By.XPATH,
    f"//td//span[contains(text(), '{name}')]",
)
