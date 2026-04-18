import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#данные
existing_task = (By.XPATH, "(//tr[contains(@id, 'job_')])[1]//a/span") #берет первую уже имеющуюся работу
random_id = random.randint(1, 10000) #рандомное имя для задачи
job_name = f"My_Job_{random_id}"
random_chars = random.choice(["?", "*", "/", ".", "!", "%", "$", '&',  ";", ":)"]) #запретные символы

#локаторы
input_field = (By.ID, "name") #поле ввода
select_new_item_button = (By.XPATH, "//a[@it]") #кнопка новой задачи

error_locator_char = (By.XPATH, '//*[@id="itemname-invalid"]')
error_locator_dub = (By.XPATH, '//*[@id="itemname-invalid"]')

freestyle_project_type = (By.CLASS_NAME, "hudson_model_FreeStyleProject")

def test_new_item_link_is_clickable(browser):

    existing_tasks = browser.find_elements(*existing_task)

    existing_task_name = None
    if len(existing_tasks) > 0:
        existing_task_name = existing_tasks[0].text
        print(f"Найдена существующая задача: {existing_task_name}")
    else:
        print("Список задач пуст, проверку на дубликат пропускаем.")

    browser.find_element(*select_new_item_button).click()
    # находим кнопку New Item и кликаем по ней
    wait = WebDriverWait(browser, 10)

    browser.find_element(*input_field).send_keys(random_chars)
    # ждем когда загрузится поле ввода и вводим текст с недопустимым символом

    error_message = wait.until(EC.visibility_of_element_located(error_locator_char))
    #отлавливаем ошибку неправильного знака
    assert "небезопасный символ" in error_message.text
    ok_button = browser.find_element(By.ID, "ok-button")
    assert not ok_button.is_enabled(), "Кнопка ОК должна быть неактивна при наличии спецсимволов"

    browser.find_element(*input_field).clear()

    if existing_task_name is not None:
        browser.find_element(*input_field).send_keys(existing_task_name)
        error_message_dub = wait.until(EC.visibility_of_element_located(error_locator_dub))
        # отлавливаем уже существующую задачу
        assert "уже существует" in error_message_dub.text
        assert not ok_button.is_enabled(), "Кнопка ОК должна быть неактивна при задаче с таким же именем"

        browser.find_element(*input_field).clear()
    else:
        print("Проверка на дубликат пропущена, так как нет существующих задач.")

    #создание новой задачи
    browser.find_element(*input_field).send_keys(job_name)
    browser.find_element(*freestyle_project_type).click()

    wait.until(lambda driver: ok_button.is_enabled())
    assert ok_button.is_enabled(), "Кнопка ОК так и не стала активной"
    ok_button.click()

    # Проверяем URL: он должен содержать имя нашей задачи и слово 'configure'
    wait.until(EC.url_contains("/configure"))
    assert "configure" in browser.current_url, "Пользователь не перенаправлен на страницу конфигурации"

    home_button = browser.find_element(By.XPATH, '//a[@class="app-jenkins-logo"]')
    home_button.click()

    assert browser.current_url == "http://localhost:8080/", "Мы не вернулись на главную панель"

    dashboard_table = browser.find_element(By.ID, "projectstatus")
    assert job_name in dashboard_table.text

