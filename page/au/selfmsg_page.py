import time

from selenium.webdriver.common.by import By

from base.au.base import BasePage, BaseHandle


class selfmsgObj(BasePage):
    def __init__(self):
        super().__init__()
        self._headimg = By.XPATH , "//*[count(child::*) = 5][1]/*[position() = 1]"
        self._chooseimg = By.XPATH , "//*[count(child::*) > 2][1]/*[position() = 1]"
        self._petname = By.XPATH , "//*[count(child::*) = 5][1]/*[position() = 3]"
        self._profile = By.XPATH , "//*[count(child::*) = 5][1]/*[position() = last()]"

    def find_headimg(self):
        return self.get_element(self._headimg)

    def find_chooseimg(self):
        return self.get_element(self._chooseimg)

    def find_petname(self):
        return self.get_element(self._petname)

    def find_profile(self):
        return self.get_element(self._profile)

class selfmsgHandle(BaseHandle):
    def __init__(self):
        self.selfmsgObj = selfmsgObj()

    def click_headimg(self):
        self.selfmsgObj.find_headimg().click()

    def click_chooseimg(self):
        self.selfmsgObj.find_chooseimg().click()

    def click_petname(self):
        self.selfmsgObj.find_petname().click()

    def click_profile(self):
        self.selfmsgObj.find_profile().click()

class selfmsgService():
    def __init__(self):
        self.selfmsgHandle = selfmsgHandle()

    def intent_headimg(self):
        self.selfmsgHandle.click_headimg()
        time.sleep(2)
        self.selfmsgHandle.click_chooseimg()

    def intent_petname(self):
        self.selfmsgHandle.click_petname()

    def intent_profile(self):
        self.selfmsgHandle.click_profile()