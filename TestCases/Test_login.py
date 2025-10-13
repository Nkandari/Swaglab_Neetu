from PageobjectModel.Loginpageobject import Loginpage

class Test_login:

 def test_login_001(self,Setup):
  Login=Loginpage(Setup)
  Login.enterusername("standard_user")
  Login.enterpassword("secret_sauce")
  Login.clickloginbtn()

 def test_login_002(self,Setup):
   Login=Loginpage(Setup)
   Login.enterusername("standard_user")
   Login.enterpassword("secret_sauce")
   Login.clickloginbtn()
   #actual_msg=Login.errormsg()
   #expected_msg="Epic sadface: Username and password do not match any user in this service"
   #assert actual_msg==expected_msg

 def test_login_003(self,Setup):
    Login=Loginpage(Setup)
    Login.login_addtocart("standard_user","secret_sauce")
    Login.clickloginbtn()

  


    