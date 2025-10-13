from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Loginpage:

    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_byid="user-name"
        self.password_textbox_byid="password"
        self.loginbtn_byid="login-button"
        self.errormsg_byxpath="//h3[@data-test='error']"

    def enterusername(self,name):
        self.driver.find_element(By.ID,self.username_textbox_byid).send_keys(name)   

    def enterpassword(self,password):
        self.driver.find_element(By.ID, self.password_textbox_byid).send_keys(password)

    def clickloginbtn(self):
        self.driver.find_element(By.ID,self.loginbtn_byid).click()

    def errormsg(self):
        error=self.driver.find_element(By.XPATH,self.errormsg_byxpath).text
        return error
    

    def errormsg(self):
        error = WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located((By.XPATH, self.errormsg_byxpath))).text
        return error
    
    def login_addtocart(self,name,password):
     self.driver.find_element(By.ID,self.username_textbox_byid).send_keys(name)  
     self.driver.find_element(By.ID,self.username_textbox_byid).send_keys(password)   
 



        