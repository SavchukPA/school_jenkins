from selenium.webdriver.common.by import By

def test_ok_button_enabled_for_folder(browser):
    element_button = browser.find_element(By.XPATH, '//a[contains(., "New Item")]')
    element_button.click()
    assert "/view/all/newJob" in browser.current_url
    element = browser.find_element (By.XPATH, "//input[@name='name']")
    element.send_keys("TestFolder")
    folder = browser.find_element(By.XPATH, "//li[contains(@class,'folder_Folder')]")
    folder.click()
    ok_button = browser.find_element(By.ID, "ok-button")
    assert ok_button.is_displayed()
