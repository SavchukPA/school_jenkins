from selenium.webdriver.common.by import By
import  time

def test_main_page_title_1(browser):
    """Тест проверки заголовка страницы"""
    browser.get("https://av.by/")
    main_page_title = "av.by — купить, продать авто в Беларуси. Автомобили с пробегом и новые."
    assert "av.by — купить, продать авто в Беларуси." in browser.title  # проверка на частичное совпадение текста
    assert main_page_title == browser.title  # проверка на полное совпадение текста


def test_cars_link(browser):
    """ Тест проверки перенаправления на страницу 'Объявления' """
    browser.get("https://av.by/")
    cars_link = browser.find_element(By.LINK_TEXT, "Объявления")
    cars_link.click()
    assert browser.current_url == "https://cars.av.by/"

    cars_page_h1_text = browser.find_element(By.TAG_NAME, "h1").text
    assert cars_page_h1_text == "Объявления о продаже автомобилей с пробегом в Беларуси"


def test_return_to_main_by_logo(browser):
    """Тест проверки возврата на главную по клику на логотип в хэдере"""
    browser.get("https://av.by/")
    cars_link = browser.find_element(By.LINK_TEXT, "Объявления")
    cars_link.click()

    logo_link = browser.find_element(By.CSS_SELECTOR, "a.header__logo-wrap")
    logo_link.click()
    assert browser.current_url == "https://av.by/"


def test_login_with_invalid_password(browser):
    """ Тест проверки текста ошибки после введения невалидного номера телефона и пароля """
    browser.get("https://av.by/")
    login_button = browser.find_element(By.LINK_TEXT, "Войти")
    login_button.click()

    phone_number_input = browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//input[@id='authPhone']")
    phone_number_input.send_keys("298734567")
    time.sleep(2)

    password_input = browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//input[@id='passwordPhone']")
    password_input.send_keys("invalid_password")
    time.sleep(2)

    submit_button_by_phone = browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//button[@type='submit' and @class='button button--action']")
    submit_button_by_phone.click()
    time.sleep(2)

    error_message_element = browser.find_element(By.CSS_SELECTOR, "div.error-message")
    assert error_message_element.text == "Неверный телефон или пароль. Если забыли пароль, восстановите его"



