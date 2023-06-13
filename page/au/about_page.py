import time

from selenium.webdriver.common.by import By
from base.au.base import BasePage, BaseHandle


class aboutObj(BasePage):
    def __init__(self):
        super().__init__()
        self._versionupdate = By.XPATH , "(//*[count(child::*)=7])/*[3]/*"

    def find_versionupdate(self):
        element = self.get_element(self._versionupdate)
        return element

class aboutHandle(BaseHandle):
    def __init__(self):
        self.aboutObj = aboutObj()

    def click_versionupdate(self):
        self.aboutObj.find_versionupdate().click()

class aboutService():
    def __init__(self):
        self.aboutHandle = aboutHandle()

    def checkupdate(self):
        self.aboutHandle.click_versionupdate()
