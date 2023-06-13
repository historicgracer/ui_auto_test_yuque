from base.au.base import BasePage,BaseHandle
from selenium.webdriver.common.by import By

class selfspaceObj(BasePage):
    def __init__(self):
        super().__init__()
        self.garden = By.XPATH , "//*[@text='我的花园']"
        self.about = By.XPATH, "(//*[count(child::*)=5])[1]/*[5]/*[last()]"

    def find_garden(self):
        return self.get_element(self.garden)

    def find_about(self):
        return self.get_element(self.about)

class selfspaceHandle(BaseHandle):
    def __init__(self):
        self.selfspaceObj = selfspaceObj()

    def click_garden(self):
        self.selfspaceObj.find_garden().click()

    def click_about(self):
        self.selfspaceObj.find_about().click()

class selfspaceService():
    def __init__(self):
        self.selfspaceHandle = selfspaceHandle()

    def intent_garden(self):
        self.selfspaceHandle.click_garden()

    def intent_about(self):
        self.selfspaceHandle.click_about()
