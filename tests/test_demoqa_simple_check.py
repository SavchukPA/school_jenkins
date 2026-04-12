# from selenium.webdriver.common.by import By
#
# def test_check_widgets_text(browser):
#     browser.get("https://demoqa.com/")
#
#     # browser.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/a[3]").click()
#     # browser.find_element(By.XPATH, "//span[text()='Alerts']").click()
#     # browser.find_element(By.ID, "confirmButton").click()
#     #
#     # alert = browser.switch_to.alert
#     # alert.accept()
#     #
#     # assert browser.find_element(By.ID, "confirmResult").text == "You selected Ok"

from selenium.webdriver.common.by import By


def test_widgets_text(browser):
    browser.get("https://demoqa.com/widgets")

    assert browser.find_element(
        By.XPATH,
        "//*[normalize-space()='Please select an item from left to start practice.']",
    ).text == "Please select an item from left to start practice."