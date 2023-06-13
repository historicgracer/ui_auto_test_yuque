from selenium.webdriver.common.by import By

from base.au.base import BasePage,BaseHandle

# 对象层
class navObj(BasePage):

    def __init__(self):
        super().__init__()
        # xpath定位方式是找到当前页面下，从顶层到深层寻找，
        # 一旦找到其子元素超过一个的的元素，那么其第二个子元素肯定是底部导航栏，根据导航栏找到对应按钮
        # 不是任何页面都有导航栏，有导航栏的时候的页面一般顶层元素都是这样结构的
        # self.selfspace = By.XPATH, "//*[count(child::) > 1][1]/child::*[2]/*[position() = last()]"
        self.selfspace = By.XPATH, "(//*[count(child::*)>1])[1]/*[2]/*[2]/*[last()]"

    def find_selfspace(self):
        return self.get_element(self.selfspace)

# 操作层
class navHandle(BaseHandle):
    def __init__(self):
        self.navObj = navObj()

    def click_selfspace(self):
        self.navObj.find_selfspace().click()
# 业务层
class navService():
    def __init__(self):
        self.navHandle = navHandle()

    def intent_selfspace(self):
        self.navHandle.click_selfspace()