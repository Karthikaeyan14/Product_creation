from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class vendorselect:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,40)
        self.select_purchase=(By.CSS_SELECTOR,"div ul li:nth-child(5) a[name='purchase']")
        self.add_vendor=(By.LINK_TEXT,"Add a line")
        self.vendor_1=self.vendor_1 = (By.XPATH, "//div[contains(@class,'o-autocomplete')]//input")
        self.dropdown_vendor=(By.XPATH,"//span[text()='OpenWood']")
        self.save=(By.CSS_SELECTOR,"button i[class='fa fa-cloud-upload fa-fw'] ")


    def vendor(self):
        self.wait.until(EC.element_to_be_clickable(self.select_purchase)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_vendor)).click()
        #time.sleep(4)
        """self.openwood=self.wait.until(EC.element_to_be_clickable(self.vendor_1))
        #self.openwood.click()
        self.openwood.send_keys("Openwood")
        self.select_dropdown=self.wait.until(EC.element_to_be_clickable(self.dropdown_vendor))
        time.sleep(4)
        self.select_dropdown.click()
        self.wait.until(EC.element_to_be_clickable(self.save)).click()

        """
        self.openwood = self.wait.until(EC.element_to_be_clickable(self.vendor_1))
        self.openwood.send_keys("Openwood")
        dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown_vendor))
        dropdown.click()
        #self.wait.until(EC.element_to_be_clickable(self.dropdown_vendor))
        self.wait.until(EC.element_to_be_clickable(self.save)).click() 