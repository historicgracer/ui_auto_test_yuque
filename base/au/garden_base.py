from selenium.webdriver.common.by import By

from WEBTestProject.base.au.base import BasePage, BaseHandle


class gardenObj(BasePage):
    def __init__(self):
        super().__init__()
        self._main = By.XPATH , "//*[count(child::*)=2][1]/*[last()]"

    def find_main(self):
        return self.get_element(self._main)

class gardenHandle(BaseHandle):
    def __init__(self):
        self.gardenObj = gardenObj()

    def scrollpage(self):
        elelocation = self.gardenObj.find_main().location
        x = elelocation["x"]
        y = elelocation["y"]
        size = self.gardenObj.find_main().size
        height = size["height"]
        width = size["width"]
        endx = x + width * 0.5
        starty = y + height * 0.9
        endy = y + height * 0.1
        self.gardenObj.driver.swipe(endx,starty,endx,endy,1500)

class gardenService():
    def __init__(self):
        self.gardenHandle = gardenHandle()