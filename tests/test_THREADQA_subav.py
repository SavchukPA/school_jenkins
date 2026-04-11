import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://lms.threadqa.ru/xpath-practice-hub")

driver.implicitly_wait(0.5)

username_box = driver.find_element(By.CSS_SELECTOR,"[data-testid='username-field']")
email_box = driver.find_element(By.CSS_SELECTOR,"[data-testid='email-field']")
password_box = driver.find_element(By.CSS_SELECTOR,"[data-testid='password-field']")
commet_box = driver.find_element(By.CSS_SELECTOR,"[data-testid='comment-field']")

username_box.send_keys("Alexander")
email_box.send_keys("test@gmail.com")
password_box.send_keys("12345678")
commet_box.send_keys("Это очень плохой тест, очень сложно и не понятно, что мы тут вообще делаем.....")
time.sleep(10)

driver.quit()


