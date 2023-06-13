import allure
from selenium.webdriver.common.by import By

from base.wu.base import BasePage, BaseHandle


class loginObj(BasePage):
    def __init__(self):
        super().__init__()
        self._switchemail = By.XPATH , "//span[@class='login-email-icon']"
        self._email = By.XPATH , "//input[@class='ant-input ant-input-lg larkui-input']"
        self._passwd = By.XPATH , "//input[@id='password']"
        self._antcheckbox = By.XPATH , "//input[@class='ant-checkbox-input']"
        self._loginbutton = By.XPATH , "//Button[@type='submit']"

    def find_switchemail(self):
        return self.get_element(self._switchemail)

    def find_email(self):
        return self.get_element(self._email)

    def find_passwd(self):
        return self.get_element(self._passwd)

    def find_antcheckbox(self):
        return self.get_element(self._antcheckbox)

    def find_loginbutton(self):
        return self.get_element(self._loginbutton)

class loginHandle(BaseHandle):
    def __init__(self):
        self.loginObj = loginObj()

    @allure.step(title="点击邮箱支付方式")
    def click_switchemail(self):
        self.loginObj.find_switchemail().click()

    @allure.step(title="点击邮箱输入框")
    def select_emailtext(self):
        self.loginObj.find_email().click()

    @allure.step(title="点击密码输入框")
    def select_passwdtext(self):
        self.loginObj.find_passwd().click()

    @allure.step(title="输入邮箱信息")
    def input_email(self,text):
        self.input_text(self.loginObj.find_email(),text)

    @allure.step(title="输入密码")
    def input_passwd(self,text):
        self.input_text(self.loginObj.find_passwd(),text)

    @allure.step(title="勾选同意协议")
    def click_antcheckbox(self):
        self.loginObj.find_antcheckbox().click()

    @allure.step(title="点击按钮登录")
    def click_loginbutton(self):
        self.loginObj.find_loginbutton().click()


class loginService():
    def __init__(self):
        self.loginHandle = loginHandle()

    def login(self,email,password):
        self.loginHandle.click_switchemail()
        self.loginHandle.select_emailtext()
        self.loginHandle.input_email(email)
        self.loginHandle.select_passwdtext()
        self.loginHandle.input_passwd(password)
        self.loginHandle.click_antcheckbox()
        self.loginHandle.click_loginbutton()
        return
