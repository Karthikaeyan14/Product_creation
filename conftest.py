import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--broswer_name", action="store", default='chrome', help="broswer selection"
    )

#main 
@pytest.fixture(scope='function')

def broswerInstance(request):
    broswer_name=request.config.getoption("broswer_name")

    if broswer_name=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)

    elif broswer_name=='firefox':
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    yield driver
    driver.quit()
    

#when we install pytest.ini for markers we need to add this function in conftest.py file
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


