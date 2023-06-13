import time

from selenium.webdriver.common.by import By

from base.wu.base import BasePage, BaseHandle


class editFileObj(BasePage):
    def __init__(self):
        super().__init__()
        self._title = By.XPATH , "//textarea[@class='ant-input lake-title']"
        self._content = By.XPATH , "//ne-p[@ne-role='render-unit']"
        self._publishbutton = By.XPATH , "//Button[@id='lake-doc-publish-button']/*[position()=1]"

    def find_title(self):
        return self.get_element(self._title)

    def find_content(self):
        return self.get_element(self._content)

    def find_publishbutton(self):
        return self.get_element(self._publishbutton)

class editFileHandle(BaseHandle):
    def __init__(self):
        self.editFileObj = editFileObj()

    def select_title(self):
        self.editFileObj.find_title().click()

    def select_content(self):
        self.editFileObj.find_content().click()

    def input_title(self, text):
        self.input_text(self.editFileObj.find_title(), text)

    def input_content(self, text):
        self.input_text_byclear(self.editFileObj.find_content(), text)

    def click_publish(self):
        self.editFileObj.find_publishbutton().click()


class editFileService():
    def __init__(self):
        self.editFileHandle = editFileHandle()

    def editFile(self):
        # self.editFileHandle.select_title()
        self.editFileHandle.input_title("test123")
        # time.sleep(1)
        self.editFileHandle.select_content()
        # time.sleep(1)
        self.editFileHandle.input_content("test123")
        # time.sleep(1)
        self.editFileHandle.click_publish()
