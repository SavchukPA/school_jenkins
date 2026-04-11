
from selenium.webdriver.common.by import By

def test_check_open_alert(browser):
    browser.get("https://demoqa.com/")

    browser.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/a[3]").click()
    browser.find_element(By.XPATH, "//span[text()='Alerts']").click()
    browser.find_element(By.ID, "confirmButton").click()

    alert = browser.switch_to.alert
    alert.accept()

    assert browser.find_element(By.ID, "confirmResult").text == "You selected Ok"



