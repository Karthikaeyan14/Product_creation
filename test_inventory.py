import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.login import Login
from pageobject.inventory import Product_create
from pageobject.inventory_purchase import vendorselect

def test_e2einventory(broswerInstance):
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