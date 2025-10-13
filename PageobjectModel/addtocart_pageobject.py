from selenium.webdriver.common.by import By

class addtocart:

  def __init__(self,driver):
   self.driver=driver  

   self.addtocart1_by_id="add-to-cart-sauce-labs-backpack"
   self.addtocart2_by_id="add-to-cart-sauce-labs-bike-light"




  def addtocartbtn1(self):
    self.driver.find_element(By.ID,self.addtocart1_by_id).click()

  def addtocartbtn2(self):
    self.driver.find_element(By.ID,self.addtocart2_by_id).click()
   
