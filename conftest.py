import pytest
from selenium import webdriver

from common.jenkins_utils import login, logout, clear_data
from common.order_utils import reorder_items_by_dependency
from common.project_utils import get_browser, get_options, get_url
from pages.new_item_page.new_item_page import NewItemPage
from utils.utils import utils
from data.test_cases.new_item import ItemTypes


@pytest.fixture(scope="function")
def driver(request):
    get_browser()

    dependency_marker = request.node.get_closest_marker("dependency")
    depends = dependency_marker.kwargs.get("depends") if dependency_marker else None
    if not depends:
        print("\nclearing data")
        clear_data()

    options = webdriver.ChromeOptions()
    for option in get_options():
        options.add_argument(option)
    print("opening browser")
    driver = webdriver.Chrome(options=options)
    print("getting page")
    driver.get(get_url())
    login(driver)
    try:
        yield driver
    finally:
        try:
            logout(driver)
        finally:
            driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    reorder_items_by_dependency(items)


@pytest.fixture()
def new_item(driver):
    folder_name = f"Test {utils.faker_en.word()}"
    description = f"Test description {utils.faker_en.word()}"
    item_type = ItemTypes.FOLDER
    new_item_page = NewItemPage(driver)
    new_item_page.create_item(
        name=folder_name, description=description, item_type=item_type
    )
    return {"name": folder_name, "description": description, "type": item_type.value}
