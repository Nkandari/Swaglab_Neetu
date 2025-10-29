from selenium.webdriver.common.by import By


class checkout:
    def __init__(self,driver):
     self.driver=driver
        
     self.firstname_byid="first-name"
     self.lastname_byid="last-name"
     self.postalcode_byid="postal-code"

    def checkout_firstname(self,firstname):
        self.driver.find_element(By.ID,self.firstname_byid).send_keys(firstname)

    def checkout_lastname(self,lastname):
        self.driver.find_element(By.ID,self.lastname_byid).send_keys(lastname)
    
    def checkout_postalcode(self,postalcode):
        self.driver.find_element(By.ID,self.postalcode_byid).send_keys(postalcode)