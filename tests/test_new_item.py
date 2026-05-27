import time

import pytest
import pages


from conftest import driver
from data.test_cases.new_item import test_cases


@pytest.mark.parametrize("test_case", test_cases)
def test_create_item(driver, test_case):
    new_item_p = pages.NewItemPage(driver=driver)
    new_item_p.create_item(
        data=test_case,
    )
    item_page = pages.ItemPage(driver=driver)
    ac_item_title = item_page.get_item_name()
    ac_item_description = item_page.get_item_description(item_type=test_case["type"])
    assert test_case["description"] in ac_item_description
    assert test_case["name"] in ac_item_title


def test_rename_item(driver, new_item):
    new_name = "New Folder"
    item_page = pages.ItemPage(driver=driver, name=new_item["name"])
    item_page.update_item(new_name="New Folder")
    ac_item_title = item_page.get_item_name()
    assert new_name in ac_item_title


def test_delete_item(driver, new_item):
    name = new_item["name"]
    item_page = pages.ItemPage(driver=driver, name=name)
    item_page.delete_item()
    time.sleep(1)
    res_delete_item = item_page.home_page.check_invisible_item_in_table(name=name)
    time.sleep(1)
    assert res_delete_item is True
