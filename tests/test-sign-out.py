from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sign_out(browser):
    user_icon = browser.find_element(By.XPATH, "//a[@class='model-link']//span")
    actions = ActionChains(browser)
    actions.move_to_element(user_icon).perform()

    wait = WebDriverWait(browser, 10)

    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tippy-1']/div/div/div/a[9]")))
    sign_out_button.click()

    sign_in_button = browser.find_element(By.XPATH, "//*[@id='main-panel']/div/form/button")
    username_field = browser.find_element(By.ID, "j_username")

    assert "login" in browser.current_url
    assert sign_in_button.is_displayed()
    assert username_field.get_attribute("value") == ""






