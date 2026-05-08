from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_sign_out(browser):
    wait = WebDriverWait(browser, 5)

    ActionChains(browser).move_to_element(
        browser.find_element(By.ID, "root-action-UserAction")
    ).perform()
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="jenkins-dropdown"]//a[@href="/logout"]')
        )
    ).click()

    assert browser.title == "Sign in - Jenkins"

    assert browser.find_element(By.ID, "j_username").get_attribute("value") == ""
    assert browser.find_element(By.ID, "j_password").get_attribute("value") == ""
