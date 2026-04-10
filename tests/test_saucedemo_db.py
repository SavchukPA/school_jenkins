
def test_login_success(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element("id", "user-name").send_keys("standard_user")
    browser.find_element("id", "password").send_keys("secret_sauce")
    browser.find_element("id", "login-button").click(),
    title = browser.find_element("class name", "title").text
    assert title == "Products"