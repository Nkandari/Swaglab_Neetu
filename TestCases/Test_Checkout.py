from PageobjectModel.Loginpageobject import Loginpage
from PageobjectModel.Cartdetails_pageobject import Cartdetails
from PageobjectModel.addtocart_pageobject import addtocart
from PageobjectModel.Checkout_pageobject import checkout
import time



class Test_checkout:


    def test_checkout(self,Setup):
     Login=Loginpage(Setup)    
     Addcart=addtocart(Setup)
     Cart=Cartdetails(Setup)
     Chkout=checkout(Setup)

     Login.enterusername("standard_user")
     Login.enterpassword("secret_sauce")
     Login.clickloginbtn()
     Addcart.addtocartbtn3()
     Addcart.addtocartbtn4()
     Cart.clickcart()
     Cart.continuebtn()
     Chkout.checkout_firstname("Neetu")
     Chkout.checkout_lastname("Kandari")
     Chkout.checkout_postalcode("248001")
     time.sleep(10)


      