import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_new_freestyle_project(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
    project_name = f"test_project_{int(time.time())}"
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(project_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Freestyle project')]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "Submit")))
    wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
    return project_name

def test_rename_freestyle_project_from_dashboard(browser):
    wait = WebDriverWait(browser, 5)
    project_name = create_new_freestyle_project(browser)
    wait.until_not(EC.url_contains('configure'))
    main_page = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'app-jenkins-logo')))
    main_page.click()
    drop_down_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="job/{project_name}/"]>.jenkins-menu-dropdown-chevron')))
    drop_down_button.click()
    rename = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Rename')))
    rename.click()
    rename_page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    assert rename_page_title.text == f'Rename Project {project_name}'




