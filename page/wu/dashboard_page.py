import time

import allure
from selenium.webdriver.common.by import By

import utils
from base.wu.base import BasePage, BaseHandle


class dashboardObj(BasePage):
    def __init__(self):
        super().__init__()
        self._popoverlist_trigger = By.XPATH , "//*[@class='QuickStart-module_itemWrapper_iYEAl larkui-popover-trigger'][1]"
        self._createfile = By.XPATH , "//*[@class='ant-menu ant-menu-root ant-menu-vertical ant-menu-light']/*[position()=1]"
        self._library = By.XPATH , "//*[@class='GlobalBookSelector-module_bookSelector_6khZ0 global-book-selector-list']/*[position()=1]"
        self._notesbutton = By.XPATH , "//span[@class='ant-menu-title-content']//*[text() = '小记']"

    def find_popoverlist_trigger(self):
        return self.get_element(self._popoverlist_trigger)

    def find_createfile(self):
        return self.get_element(self._createfile)

    def find_library(self):
        return self.get_element(self._library)

    def find_notesbutton(self):
        return self.get_element(self._notesbutton)

class dashboardHandle(BaseHandle):
    def __init__(self):
        self.dashboardObj = dashboardObj()

    @allure.step(title="鼠标移动并悬停到下拉菜单")
    def moveToPopoverList(self):
        self.move_mouse(self.dashboardObj.find_popoverlist_trigger(),self.dashboardObj.driver)

    @allure.step(title="鼠标移动并悬停到新建文档")
    def moveToPopover(self):
        self.move_mouse(self.dashboardObj.find_createfile(),self.dashboardObj.driver)

    @allure.step(title="点击下拉菜单中的新建文档")
    def click_popover(self):
        self.dashboardObj.find_createfile().click()

    @allure.step(title="点击默认知识库")
    def click_library(self):
        self.dashboardObj.find_library().click()

    @allure.step(title="点击小记子导航")
    def click_notesbutton(self):
        self.dashboardObj.find_notesbutton().click()

class dashboardService():
    def __init__(self):
        self.dashboardHandle = dashboardHandle()

    def intent_File(self):
        self.dashboardHandle.moveToPopoverList()
        time.sleep(1)
        self.dashboardHandle.moveToPopover()
        time.sleep(1)
        self.dashboardHandle.click_popover()
        time.sleep(1)
        self.dashboardHandle.click_library()


    def intent_Notes(self):
        time.sleep(1)
        self.dashboardHandle.click_notesbutton()