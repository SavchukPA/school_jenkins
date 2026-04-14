from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ya.ru")

# Проверка: слово "Яндекс" есть в заголовке страницы
assert "Яндекс" in driver.title

driver.quit()