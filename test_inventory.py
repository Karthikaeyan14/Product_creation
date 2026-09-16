from typing import Any

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.login import Login
from pageobject.inventory import Product_create
from pageobject.inventory_purchase import vendorselect

def test_e2einventory(broswerInstance: WebDriver | WebDriver | Any):
    driver=broswerInstance
    driver.get("https://115749520-19-0-all.runbot201.odoo.com/")
    login=Login(driver)
    login.signup()
    login.login_details("admin","admin")
    inventory=Product_create(driver)
    inventory.product()
    inventory.product_details("product_6","15","8")
    inventory.category()
    inventory.tracking('IR001')
    inve_pur=vendorselect(driver)
    inve_pur.vendor()

@pytest.mark.invalid
def test_invalidlogin(broswerInstance: WebDriver | WebDriver | Any):
    driver=broswerInstance
    driver.get("https://125358134-19-0-all.runbot110.odoo.com/")
    login=Login(driver)
    #login.signup()
    login.signup()
    login.login_details("admin","admin123")
    warning_message_text = login.warning_message()
    assert warning_message_text == "Wrong login/password"