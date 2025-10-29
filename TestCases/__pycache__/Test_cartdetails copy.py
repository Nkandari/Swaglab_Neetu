from PageobjectModel.Loginpageobject import Loginpage
from PageobjectModel.Cartdetails_pageobject import Cartdetails
from PageobjectModel.addtocart_pageobject import addtocart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures("Setup")
 
@pytest.mark.MySetup 
class Test_cartdetailspage:
  def test_cartdetail01(self,Setup):    
    Login=Loginpage(Setup)
    Addcart=addtocart(Setup)
    Cart=Cartdetails(Setup)
    wait = WebDriverWait(Setup, 10)


    Login.enterusername("standard_user")
    Login.enterpassword("secret_sauce")
    Login.clickloginbtn()
    #Addcart.addtocartbtn1()
    #Addcart.addtocartbtn2()
   # Addcart.addtocartbtn3()
   # Addcart.addtocartbtn4()
    #time.sleep(5)
    #Cart.clickcart()
    #time.sleep(5)
   
    Addcart.addtocartbtn3()
    Addcart.addtocartbtn4()
    time.sleep(10)

    

    Cart.clickcart()

  
    '''Login.enterusername("standard_user")
    Login.enterpassword("secret_sauce")
    Login.clickloginbtn()
    wait = WebDriverWait(Setup, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    Addcart.addtocartbtn1()
    Addcart.addtocartbtn2()
    wait = WebDriverWait(Setup, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    Cart.clickcart()'''
    

        



