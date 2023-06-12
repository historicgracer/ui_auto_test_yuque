from selenium.webdriver.common.by import By
from WEBTestProject.base.au.base import BasePage, BaseHandle


class editProfileObj(BasePage):
    def __init__(self):
        super().__init__()
        self._textarea = By.XPATH , "//*[@class='android.widget.EditText']"
        self._donebutton = By.XPATH , "//*[@class='android.widget.TextView' and @text='完成']"

    def find_textarea(self):
        element = self.get_element(self._textarea)
        return element

    def find_donebutton(self):
        element = self.get_element(self._donebutton)
        return element

class editProfileHandle(BaseHandle):
    def __init__(self):
        self.editProfileObj = editProfileObj()

    def input_profile(self,text):
        self.input_text(self.editProfileObj.find_textarea(),text)

    def click_done(self):
        self.editProfileObj.find_donebutton().click()

class editProfileService():
    def __init__(self):
        self.editProfileHandle = editProfileHandle()

    def modProfileMsg(self,text):
        self.editProfileHandle.input_profile(text)
        self.editProfileHandle.click_done()