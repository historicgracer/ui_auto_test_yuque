import logging
import time

import allure
import pytest

from page.wu.dashboard_page import dashboardService
from page.wu.login_page import loginService
from utils import UtilsDriver,get_test_data

data = get_test_data("/data/wu/test_login.json")

@pytest.mark.run(order=1002)
class TestLogin:
    def setup_class(self):
        self.loginService = loginService()
        self.dashboardService = dashboardService()

    def teardown_class(self):
        UtilsDriver.quit_wu_driver()

    @UtilsDriver.capture_screenshot_on_failure
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("email,password,expect",data)
    def test_login(self,email,password,expect):
        print(data)
        logging.info("用例的数据如下：邮箱：{}，密码：{}，顶期结果：{}".format(email,password,expect))
        # logger.
        time.sleep(2)
        self.loginService.login(email,password)
        allure.attach(UtilsDriver.get_wu_driver().get_screenshot_as_png(),"登录截图", allure.attachment_type.PNG)