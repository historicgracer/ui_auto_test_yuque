
import time

import pytest

from page.wu.dashboard_page import dashboardService
from page.wu.edit_file_page import editFileService
from utils import UtilsDriver


@pytest.mark.run(order=1003)
class TestModUser:
    def setup_class(self):
        self.dashboardService = dashboardService()
        self.editFileService = editFileService()
        UtilsDriver.open_wu_window()

    def teardown_class(self):
        UtilsDriver.quit_wu_driver()

    @UtilsDriver.capture_screenshot_on_failure
    def test_publishFile(self):
        self.dashboardService.intent_File()
        time.sleep(3)
        self.editFileService.editFile()
        time.sleep(3)
        UtilsDriver.close_window()
        UtilsDriver.switch_to_window()
