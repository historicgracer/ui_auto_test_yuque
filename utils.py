import functools
import inspect
import json
import os
import time
from datetime import datetime

from appium import webdriver as au_driver
from selenium import webdriver as wu_driver

from config import BaseDir


class UtilsDriver:
    _au_driver = None
    _wu_driver = None
    original_tab_handle = None
    _testdone = True #执行多个用例之前

    @classmethod
    def get_au_driver(cls):
        if cls._au_driver is None:
            config_str = {
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "emulator-5554",
                "appPackage": "com.yuque.mobile.android.app",
                "appActivity": ".rn.activity.ReactNativeMainActivity",
                "noReset":True,
                "resetKeyboard": True,
                "unicodeKeyboard": True,
                "automationName": "Uiautomator2"
            }
            cls._au_driver = au_driver.Remote('http://localhost:4723/wd/hub', config_str)
        return cls._au_driver

    @classmethod
    def get_wu_driver(cls):
        if cls._wu_driver is None:
            cls._wu_driver = wu_driver.Edge()
            cls._wu_driver.maximize_window()
            cls._wu_driver.get("https://www.yuque.com/login")
            # cls._wu_driver.get("https://www.yuque.com/login?goto=https%3A%2F%2Fwww.yuque.com%2Fdashboard")
            cls.original_tab_handle = cls._wu_driver.current_window_handle
        # print('cls',cls._driver,id(cls._driver))
        return cls._wu_driver

    @classmethod
    def quit_au_driver(cls):
        if cls._au_driver is not None and cls._testdone:
            cls._au_driver.quit()
            cls._au_driver = None

    @classmethod
    def quit_wu_driver(cls):
        if cls._wu_driver is not None and cls._testdone:
            cls._wu_driver.quit()
            cls._wu_driver = None

    @staticmethod
    def capture_screenshot_on_failure(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                screenshot_name = f"image/{inspect.stack()[1][3]}_{now}.png"
                UtilsDriver.get_wu_driver().get_screenshot_as_file(screenshot_name)
                # args[0].driver.get_screenshot_as_file(screenshot_name)
                print("截图好了。。。。")
                raise e

        return wrapper

    @classmethod
    def open_wu_window(cls):
        print("utils========",cls._wu_driver.current_window_handle)
        cls._wu_driver.execute_script("window.open(arguments[0]);", cls._wu_driver.current_url)
        # cls._wu_driver.execute_script("window.open();")

    @classmethod
    def switch_to_window(cls):
        cls._wu_driver.switch_to.window(cls._wu_driver.window_handles[-1])
        # current_handle= cls._wu_driver.current_window_handle
        # handles = cls._wu_driver.window_handles
        # for handle in handles:
        #     if handle != current_handle:
        #         cls._wu_driver.switch_to.window(handle)
        #         break

    @classmethod
    def close_window(cls):
        if len(cls._wu_driver.window_handles) > 1:
            cls._wu_driver.close()

def get_test_data(filename):
    filename = BaseDir + filename
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
    temp = []
    for i in case.values():
        temp.append(tuple(i.values()))

    return temp

print(get_test_data("/data/wu/test_login.json"))


