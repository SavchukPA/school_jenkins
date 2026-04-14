import time

from selenium.webdriver.common.by import By

demoqa_url = "https://demoqa.com/"

def test_check_open_alert(browser):
    browser.get(demoqa_url)

    browser.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/a[3]").click()
    browser.find_element(By.XPATH, "//span[text()='Alerts']").click()
    browser.find_element(By.ID, "confirmButton").click()

    alert = browser.switch_to.alert
    alert.accept()

    assert browser.find_element(By.ID, "confirmResult").text == "You selected Ok"

def test_check_switch_new_tab(browser):
    browser.get(demoqa_url)

    browser.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/a[3]").click()
    browser.find_element(By.XPATH, "//span[text()='Browser Windows']").click()
    browser.find_element(By.ID, "tabButton").click()

    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[1])

    assert browser.find_element(By.ID, "sampleHeading").text == "This is a sample page"

