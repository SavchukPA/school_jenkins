
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_navigation_to_manage_page(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction"))).click()

    wait.until(EC.url_contains("/manage"))

    assert "/manage" in browser.current_url



def test_manaje_jenkins_icon_is_visible(browser):
    wait = WebDriverWait(browser, 10)

    assert wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))).is_displayed()