from WEBTestProject.utils import UtilsDriver
import pytest

@pytest.mark.run(order=2000)
class TestEnd:
    def test_end(self):
        UtilsDriver._testdone = True
        UtilsDriver.quit_wu_driver()