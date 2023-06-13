
from utils import UtilsDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_au_driver()

    def get_element(self,path):
        print("怎么啦？",path)
        wait = WebDriverWait(self.driver,10,1)
        element = wait.until(lambda x:x.find_element(*path))
        print("有问题吗？？？？")
        return element

class BaseHandle:
    def input_text(self,element,content):
        element.clear()
        element.send_keys(content)

