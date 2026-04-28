from selenium.webdriver.common.by import By


def _get_rest_api_link(driver):
    locator = (By.XPATH, '//footer//a[text()="REST API"]')
    return driver.find_element(*locator)


def _get_manage_jenkins_button(driver):
    manage_jenkins_button = (By.ID, 'root-action-ManageJenkinsAction')
    return driver.find_element(*manage_jenkins_button)


def _get_jenkins_logo(driver):
    jenkins_logo = (By.CSS_SELECTOR, '.app-jenkins-logo span')
    return driver.find_element(*jenkins_logo)


def test_checking_the_button_on_dashboard(browser):

    assert _get_rest_api_link(browser).is_displayed()


def test_checking_the_button_on_nodes(browser):
    _get_manage_jenkins_button(browser).click()
    browser.find_element(By.CSS_SELECTOR, 'a[href="computer"]').click()

    assert _get_rest_api_link(browser).is_displayed()


def test_checking_the_button_on_credentials(browser):
    _get_manage_jenkins_button(browser).click()
    browser.find_element(By.CSS_SELECTOR, 'a[href="credentials"]').click()

    assert _get_rest_api_link(browser).is_displayed()


def test_checking_rest_api_documentation_on_main_page(browser):
    _get_rest_api_link(browser).click()
    crumb = browser.find_element(By.ID, 'breadcrumbs').find_element(By.TAG_NAME, 'li')

    assert "API" in crumb.text
    assert "Jenkins" in _get_jenkins_logo(browser).text