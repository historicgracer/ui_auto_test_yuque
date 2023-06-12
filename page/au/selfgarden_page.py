from selenium.webdriver.common.by import By
from WEBTestProject.base.au.garden_base import gardenObj, gardenHandle


class selfgardenObj(gardenObj):
    def __init__(self):
        super().__init__()
        self.modbutton = By.XPATH , "//*[@class='android.widget.Button' and @text='编辑资料']"
        # self.modbutton = By.XPATH , "//*[@class='android.widget.Button'][1]"

    def find_modbutton(self):
        element = self.get_element(self.modbutton)
        return element

class selfgardenHandle(gardenHandle):
    def __init__(self):
        super().__init__()
        self.selfgardenObj = selfgardenObj()

    def click_modbutton(self):
        self.selfgardenObj.find_modbutton().click()

class selfgardenService():
    def __init__(self):
        self.selfgardenHandle = selfgardenHandle()

    def intent_selfmsg(self):
        self.selfgardenHandle.click_modbutton()

    def scroll_page(self):
        self.selfgardenHandle.scrollpage()