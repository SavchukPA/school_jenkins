from selenium.webdriver.common.by import By
from conftest import browser


def _get_field_search(driver):
    return driver.find_element(By.ID, 'settings-search-bar')


def test_checking_the_dropdown_when_entering_one_letter(browser):
    browser.find_element(By.ID, 'root-action-ManageJenkinsAction').click()

    _get_field_search(browser).send_keys('t')
    items = browser.find_elements(
        By.XPATH,
        '//*[contains(@class, "jenkins-search__results-container--visible")]//a[contains(translate(., "T", "t"), "t")]'
    )

    assert len(items) > 1