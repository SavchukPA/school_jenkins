
from selenium.webdriver.common.by import By

def test_jenkins_ns(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys("test_1")
    browser.find_element(By.XPATH, "//[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.ID, "name='Submit").click()
    label=browser.find_element(By.ID,"job-index-headline page-headline")

    assert label.text == "test_1"