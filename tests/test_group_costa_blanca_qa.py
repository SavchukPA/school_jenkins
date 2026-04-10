from selenium.webdriver.common.by import By


def test_storyia_submit_form(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = browser.find_element(By.NAME, "my-text")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Storyia")
    submit_button.click()

    message = browser.find_element(By.ID, "message").text

    assert message == "Received!"

def test_storyia_checkbox_selected(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    checkbox = browser.find_element(By.ID, "my-check-2")
    checkbox.click()

    assert checkbox.is_selected()

    #########################################################################

    from selenium.webdriver.common.by import By
    import time

    def test_tittle_sergio_qa(browser):
        '''Тест проверки заголовка страницы'''
        browser.get('https://martspec.com/')
        assert 'Simplify health & wellness tracking' in browser.title

    def test_change_language_sergio_qa(browser):
        '''Раскрыть список языков веб-сайта'''
        browser.get('https://martspec.com/')

        dropdown = browser.find_element(By.ID, 'navbarDropdown')
        dropdown.click()

        time.sleep(3)

