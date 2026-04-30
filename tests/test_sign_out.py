from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sign_out(browser):
    user_icon = browser.find_element(By.XPATH, "//a[@class='model-link']//span")
    actions = ActionChains(browser)
    actions.move_to_element(user_icon).perform()

    wait = WebDriverWait(browser, 10)

    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/logout')]")))
    sign_out_button.click()

    username_field = browser.find_element(By.ID, "j_username")
    password_field = browser.find_element(By.ID, "j_password")

    assert username_field.get_attribute("value") == ""
    assert password_field.get_attribute("value") == ""






