from selenium import webdriver
import pytest




@pytest.fixture(scope="class")
def Setup(request):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield driver
    driver.quit()
'''
@pytest.fixture()
def Setup():
   driver_path = "Drivers\msedgedriver.exe"
   driver=webdriver.Edge(executable_path=driver_path)
   driver.maximize_window()
   driver.get("https://www.saucedemo.com/")
   
   yield driver
   driver.quit()'''