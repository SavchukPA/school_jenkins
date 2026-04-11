import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By



def test_docker():
    driver = webdriver.Chrome()

    search_text = ""
    target_text = "Jenkins is an open-source automation server that enables developers to build, test, and deploy their software efficiently. It supports continuous integration and continuous deployment (CI/CD) workflows with extensive plugin ecosystem and distributed build capabilities."

    try:

        driver.get("https://hub.docker.com")

        driver.implicitly_wait(2)
        count = 0
        while count <= 5:
            try:
                driver.find_element(by=By.XPATH, value="//p[text()='Search Docker Hub']/..").click()
                break
            except StaleElementReferenceException:
                count += 1

        text_box = driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Docker Hub']")
        text_box.send_keys("jenkins")
        text_box.send_keys(Keys.ENTER)
        time.sleep(1)
        count = 0
        while count <= 5:
            try:
                search_text = driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Jenkins is an open-source automation server that enables developers to build')]")
                break
            except Exception:
                count += 1

        out_text = search_text.text

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()

        assert target_text in out_text


if __name__ == "__main__":
    test_docker()
