import time

from selenium.webdriver.common.by import By
from base.au.base import BasePage, BaseHandle


class editImgObj(BasePage):
    def __init__(self):
        super().__init__()
        self._imgredio = By.XPATH , "//*[@resource-id='radio-btn'][1]"
        self._donebutton = By.XPATH , "(//*[count(child::*)=3])[1]/*[last()]//*[starts-with(@text,'完成')]"
        self._finaldonebutton = By.XPATH , "(//*[count(child::*)=5])[1]/*[last()]"

    def find_imgredio(self):
        element = self.get_element(self._imgredio)
        return element

    def find_donebutton(self):
        element = self.get_element(self._donebutton)
        return element

    def find_finaldonebutton(self):
        element = self.get_element(self._finaldonebutton)
        return element

class editImgHandle(BaseHandle):
    def __init__(self):
        self.editImgObj = editImgObj()

    def click_img(self):
        self.editImgObj.find_imgredio().click()

    def click_done(self):
        self.editImgObj.find_donebutton().click()

    def click_finaldone(self):
        self.editImgObj.find_finaldonebutton().click()

class editImgService():
    def __init__(self):
        self.editImgHandle = editImgHandle()

    def modImgMsg(self):
        self.editImgHandle.click_img()
        time.sleep(1)
        self.editImgHandle.click_done()
        time.sleep(1)
        self.editImgHandle.click_finaldone()