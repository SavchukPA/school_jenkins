from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_new_item_page(browser):
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.url_contains("/newJob")
    )

    assert "/newJob" in browser.current_url