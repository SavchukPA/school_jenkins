import time
import pytest

from conftest import driver
from pages.new_item_page.new_item_page import NewItemPage
from pages.item_page.item_page import ItemPage


@pytest.mark.dependency(name="test_create_item")
def test_create_item(driver):
    ex_test_folder_name = "Test Folder"
    ex_test_folder_description = "Test Folder Description"
    new_item_p = NewItemPage(driver=driver)
    new_item_p.create_item(
        name=ex_test_folder_name,
        description=ex_test_folder_description,
        type_item="Folder",
    )
    item_page = ItemPage(driver=driver)
    ac_item_title = item_page.get_item_name()
    ac_item_description = item_page.get_item_description()
    assert ex_test_folder_description in ac_item_description
    assert ex_test_folder_name in ac_item_title


@pytest.mark.dependency(name="test_rename_item", depends=["test_create_item"])
def test_rename_item(driver):
    current_name = "Test Folder"
    new_name = "New Folder"
    item_page = ItemPage(driver=driver, name=current_name)
    item_page.update_item(new_name=new_name)
    ac_item_title = item_page.get_item_name()

    assert new_name in ac_item_title


@pytest.mark.dependency(name="delete_item", depends=["test_rename_item"])
def test_delete_item(driver):
    name = "New Folder"
    item_page = ItemPage(driver=driver, name=name)
    item_page.delete_item()
    time.sleep(1)
    res_delete_item = item_page.home_page.check_invisible_item_in_table(name=name)
    assert res_delete_item is True
