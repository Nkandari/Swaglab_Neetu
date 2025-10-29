from PageobjectModel.Loginpageobject import Loginpage
from PageobjectModel.Cartdetails_pageobject import Cartdetails
from PageobjectModel.addtocart_pageobject import addtocart

import time

class Test_cartdetailspage:
  def test_cartdetail01(self,Setup):
    Login=Loginpage(Setup)    
    Addcart=addtocart(Setup)
    Cart=Cartdetails(Setup)
    Login.enterusername("standard_user")
    Login.enterpassword("secret_sauce")
    Login.clickloginbtn()
  
    time.sleep(1)
    
    Addcart.addtocartbtn3()
    Addcart.addtocartbtn4()
    time.sleep(1)
    
    Cart.clickcart()
    Cart.continuebtn()
    time.sleep(10)