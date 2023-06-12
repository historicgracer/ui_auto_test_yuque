from WEBTestProject.utils import UtilsDriver
import pytest

@pytest.mark.run(order=1001)
class TestBegin:
    def test_begin(self):
        UtilsDriver._testdone = False