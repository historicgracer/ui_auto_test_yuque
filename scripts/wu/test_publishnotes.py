import time

import allure
import pytest

from WEBTestProject.page.wu.dashboard_page import dashboardService
from WEBTestProject.page.wu.notes_page import notesService
from WEBTestProject.utils import UtilsDriver,get_test_data

data = get_test_data("/data/wu/test_notes.json")

@pytest.mark.run(order=1004)
class TestPublishNotes:
    def setup_class(self):
        self.dashboardService = dashboardService()
        self.notesService = notesService()

    def teardown_class(self):
        UtilsDriver.quit_wu_driver()

    @UtilsDriver.capture_screenshot_on_failure
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("content,picture,expect",data)
    def test_publishnotes(self,content,picture,expect):
        time.sleep(2)
        self.dashboardService.intent_Notes()
        time.sleep(2)
        self.notesService.publish_notes(content,picture)
        time.sleep(3)
        allure.attach(UtilsDriver.get_wu_driver().get_screenshot_as_png(),"小记截图", allure.attachment_type.PNG)
        assert expect == self.notesService.notesHandle.check_result()
