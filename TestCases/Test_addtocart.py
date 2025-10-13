from PageobjectModel.Loginpageobject import Loginpage
from PageobjectModel.addtocart_pageobject import addtocart
import time

class Test_addtocartpage:

 def test_additem001(self,Setup):
  cart=addtocart(Setup)
  Login=Loginpage(Setup)
  Login.enterusername("standard_user")
  Login.enterpassword("secret_sauce")
  Login.clickloginbtn()
  cart.addtocartbtn1()
  cart.addtocartbtn2()
  time.sleep(10)

  

