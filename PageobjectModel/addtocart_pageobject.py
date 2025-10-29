from selenium.webdriver.common.by import By

class addtocart:

  def __init__(self,driver):
   self.driver=driver  

   '''self.addtocart1_by_id="add-to-cart-sauce-labs-backpack"
   self.addtocart2_by_id="add-to-cart-sauce-labs-bike-light"'''
   
   self.addtocart3_by_id="add-to-cart-sauce-labs-bolt-t-shirt"
   self.addtocart4_by_id="add-to-cart-sauce-labs-fleece-jacket"



  '''def addtocartbtn1(self):
    self.driver.find_element(By.ID,self.addtocart1_by_id).click()

  def addtocartbtn2(self):
    self.driver.find_element(By.ID,self.addtocart2_by_id).click()
   '''
  def addtocartbtn3(self):
    self.driver.find_element(By.ID,self.addtocart3_by_id).click()


  def addtocartbtn4(self):
    self.driver.find_element(By.ID,self.addtocart4_by_id).click()
