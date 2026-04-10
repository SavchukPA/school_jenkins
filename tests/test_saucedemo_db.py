import pytest

@pytest.fixture(autouse=True)
def open_site(browser):
    browser.get("https://www.saucedemo.com")

def test_login_success(browser):
    browser.find_element("id", "user-name").send_keys("standard_user")
    browser.find_element("id", "password").send_keys("secret_sauce")
    browser.find_element("id", "login-button").click(),
    title = browser.find_element("class name", "title").text
    assert title == "Products"

def test_login_wrong_password(browser):
    browser.find_element("id", "user-name").send_keys("standard_user")
    browser.find_element("id", "password").send_keys("wrong_password")
    browser.find_element("id", "login-button").click(),
    error = browser.find_element("class name", "error-message-container").text
    assert "Epic sadface" in error

def test_login_empty_fields(browser):
    browser.find_element("id", "login-button").click()
    error = browser.find_element("class name", "error-message-container").text
    assert "Epic sadface" in error