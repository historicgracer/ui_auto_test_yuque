import time

import autoit
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from WEBTestProject.utils import UtilsDriver
from WEBTestProject.base.wu.base import BasePage, BaseHandle


class notesObj(BasePage):
    def __init__(self):
        super().__init__()
        self._picbutton = By.XPATH , "//button[@class = 'ant-btn ne-ui-toolbar-file-button ne-ui-toolbar-image ne-toolbar-widget ne-ui-t-button']"
        self._content = By.XPATH , "//div[@class = 'ne-engine ne-typography-classic ne-active']"
        self._notify = By.XPATH , "//div[@class = 'ant-message']//span[last()]"

    def find_picbutton(self):
        return self.get_element(self._picbutton)

    def find_content(self):
        return self.get_element(self._content)

    def find_notify(self):
        return self.get_element(self._notify)

class notesHandle(BaseHandle):
    def __init__(self):
        self.notesObj = notesObj()

    def click_picbutton(self):
        action = ActionChains(UtilsDriver.get_wu_driver())
        action.click(self.notesObj.find_picbutton()).perform()

    def select_content(self):
        self.notesObj.find_content().click()

    def input_content(self,text):
        self.input_text(self.notesObj.find_content(),text)

    def upload_file(self,text):
        autoit.win_wait_active("打开",3)
        # autoit.control_send("打开","Edit1",text)
        time.sleep(1)
        autoit.control_set_text("打开","Edit1",text)
        autoit.control_click("打开","Button1")

    def create_notes(self):
        actions = ActionChains(UtilsDriver.get_wu_driver())
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

    def check_result(self):
        return self.notesObj.find_notify().text

class notesService():
    def __init__(self):
        self.notesHandle = notesHandle()

    def publish_notes(self,content,picture):
        self.notesHandle.select_content()
        self.notesHandle.input_content(content)
        self.notesHandle.click_picbutton()
        self.notesHandle.upload_file(picture)
        time.sleep(2)
        self.notesHandle.create_notes()
        # assert self.notesHandle.check_result() in "内容发布成功"
