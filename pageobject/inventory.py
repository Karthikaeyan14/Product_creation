from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Product_create:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,40)
        self.click_inventory=(By.CSS_SELECTOR,"a[href='/odoo/inventory']")
        self.product_0=(By.XPATH,"//button //span[text()='Products']")
        self.product_1=(By.XPATH,"//div //a[text()='Products'] ")
        self.new_product=(By.XPATH,"//div //button[text()=' New '] ")
        self.enter_product=(By.XPATH,"//div //textarea[@id='name_0'] ")
        self.sales_price=(By.ID,"list_price_0")
        self.unit_price=(By.CSS_SELECTOR,"div input[id='standard_price_0']")
        self.select_category=(By.CSS_SELECTOR,"div input[id='categ_id_0']")
        self.click_category=(By.CSS_SELECTOR,"li a[id ='categ_id_0_0_0']")
        self.track=(By.CSS_SELECTOR,"div input[id='tracking_1']")
        self.tracking_type=(By.XPATH,"//div [@role='menu']//span[@data-choice-index='1'] //div[text()='By Lots']")
        self.reference=(By.CSS_SELECTOR,"div input[id='default_code_0']")
        self.save=(By.CSS_SELECTOR,"button i[class='fa fa-cloud-upload fa-fw'] ")
    


    def product(self):
        self.wait.until(EC.element_to_be_clickable(self.click_inventory)).click()
        self.wait.until(EC.element_to_be_clickable(self.product_0)).click()
        self.wait.until(EC.element_to_be_clickable(self.product_1)).click()
        self.wait.until(EC.element_to_be_clickable(self.new_product)).click()

    def product_details(self,product_name,sp,up):
        productname=self.wait.until(EC.element_to_be_clickable(self.enter_product)).send_keys(product_name)
        saleprice=self.wait.until(EC.element_to_be_clickable(self.sales_price))
        saleprice.clear()
        saleprice.send_keys(sp)
        unitprice=self.wait.until(EC.element_to_be_clickable(self.unit_price))
        unitprice.clear()
        unitprice.send_keys(up)
        #self.wait.until(EC.element_to_be_clickable(self.save)).click()
    
    def category(self):
        category=self.wait.until(EC.element_to_be_clickable(self.select_category))
        category.send_keys("Clothes")
        select_dropdown_category=self.wait.until(EC.element_to_be_clickable(self.click_category))
        select_dropdown_category.click()
        self.wait.until(EC.element_to_be_clickable(self.save)).click()
    
    def tracking(self,IR):
        click_tracking=self.wait.until(EC.element_to_be_clickable(self.track))
        click_tracking.click()
        select_tracking=self.wait.until(EC.element_to_be_clickable(self.tracking_type))
        select_tracking.click()
        Internalreference=self.wait.until(EC.presence_of_element_located(self.reference))
        Internalreference.send_keys(IR)

