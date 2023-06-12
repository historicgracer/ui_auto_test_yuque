#
# import time
#
# import pytest
#
# from WEBTestProject.base.au.nav_base import navService
# from WEBTestProject.page.au.about_page import aboutService
# from WEBTestProject.page.au.selfspace_page import selfspaceService
# from WEBTestProject.utils import UtilsDriver
#
#
# @pytest.mark.run(order=3)
# class TestModUser:
#     def setup_class(self):
#         self.nav_service = navService()
#         self.selfspace_service = selfspaceService()
#         self.about_Service = aboutService()
#
#     def teardown_class(self):
#         UtilsDriver.quit_au_driver()
#
#     def test_moduser(self):
#         self.nav_service.intent_selfspace()
#         time.sleep(1)
#         self.selfspace_service.intent_about()
#         time.sleep(3)
#         self.about_Service.checkupdate()
#         time.sleep(3)
#         print(self.about_Service.aboutHandle.aboutObj.get_element("暂无新版本"))
#
