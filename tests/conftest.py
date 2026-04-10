import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# scope="function" означает, что фикстура будет срабатывать перед КАЖДЫМ тестом
# и закрывать браузер после КАЖДОГО теста, как методы BeforeMethod / AfterMethod в Java
@pytest.fixture(scope="function")
def browser():
    """Открытие и закрытие браузера перед и после каждого теста"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # для фонового режима
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    # Код ДО 'yield' выполняется перед тестом (как @Before / setUp)
    yield driver
    
    # Код ПОСЛЕ 'yield' выполняется после теста (как @After / tearDown)
    driver.quit()
