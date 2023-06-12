#
# import time
#
# import pytest
#
# from WEBTestProject.page.wu.dashboard_page import dashboardService
# from WEBTestProject.page.wu.edit_file_page import editFileService
# from WEBTestProject.utils import UtilsDriver
#
#
# @pytest.mark.run(order=1003)
# class TestModUser:
#     def setup_class(self):
#         self.dashboardService = dashboardService()
#         self.editFileService = editFileService()
#
#     def teardown_class(self):
#         UtilsDriver.quit_wu_driver()
#
#     @UtilsDriver.capture_screenshot_on_failure
#     def test_publishFile(self):
#         self.dashboardService.intent_File()
#         time.sleep(3)
#         self.editFileService.editFile()
#         time.sleep(3)