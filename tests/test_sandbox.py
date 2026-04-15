from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_validation_form(browser):
    password = "password1"
    browser.get("https://aqa-proka4.org/sandbox/web")
    browser.find_element(By.ID, "val-username").send_keys("Emilia")
    browser.find_element(By.ID, "val-email").send_keys("emilia@mail.ru")
    browser.find_element(By.ID, "val-password").send_keys(password)
    browser.find_element(By.ID, "val-confirm-password").send_keys(password)
    browser.find_element(By.ID, "valSubmitBtn").click()
    success_element = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='valFormResult']/div/p"))
    )
    assert "Все проверки пройдены! Форма валидна." in success_element.text, \
        f"Ожидалось сообщение об успехе, получили: '{success_element.text}'"