from selenium.webdriver.common.by import By

class Cartdetails:

    def __init__(self,driver):

        self.driver=driver
       # self.carticon_byxpath="//a[@class='shopping_cart_link']"
       # self.carticon_byid="shopping_cart_container"
        self.carticon_byxpath = "//a[@class='shopping_cart_link']"
        #self.carticon_byid="add-to-cart-sauce-labs-bolt-t-shirt"
        self.continue_byid="checkout"



    def clickcart(self):
        self.driver.find_element(By.XPATH,self.carticon_byxpath).click()

    def continuebtn(self):
        self.driver.find_element(By.ID,self.continue_byid).click()


    
