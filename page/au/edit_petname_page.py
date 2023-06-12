from selenium.webdriver.common.by import By
from WEBTestProject.base.au.base import BasePage, BaseHandle


class editPetnameObj(BasePage):
    def __init__(self):
        super().__init__()
        self._textarea = By.XPATH , "//*[@class='android.widget.EditText']"
        self._donebutton = By.XPATH , "//*[@class='android.widget.TextView' and @text='完成']"

    def find_textarea(self):
        element = self.get_element(self._textarea)
        print("find_textarea",element)
        return element

    def find_donebutton(self):
        element = self.get_element(self._donebutton)
        print("find_donebutton",element)
        return element

class editPetnameHandle(BaseHandle):
    def __init__(self):
        self.editPetnameObj = editPetnameObj()

    def input_petname(self,text):
        self.input_text(self.editPetnameObj.find_textarea(),text)

    def click_done(self):
        self.editPetnameObj.find_donebutton().click()

class editPetnameService():
    def __init__(self):
        self.editPetnameHandle = editPetnameHandle()

    def modPetname(self,text):
        self.editPetnameHandle.input_petname(text)
        self.editPetnameHandle.click_done()