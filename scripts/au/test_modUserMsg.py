#
# import time
#
# import pytest
#
# from WEBTestProject.base.au.nav_base import navService
# from WEBTestProject.page.au.edit_img import editImgService
# from WEBTestProject.page.au.edit_petname_page import editPetnameService
# from WEBTestProject.page.au.edit_profile_page import editProfileService
# from WEBTestProject.page.au.selfgarden_page import selfgardenService
# from WEBTestProject.page.au.selfmsg_page import selfmsgService
# from WEBTestProject.page.au.selfspace_page import selfspaceService
# from WEBTestProject.utils import UtilsDriver
#
#
# @pytest.mark.run(order=2)
# class TestModUser:
#     def setup_class(self):
#         self.nav_service = navService()
#         self.selfspace_service = selfspaceService()
#         self.selfgarden_service = selfgardenService()
#         self.selfmsg_service = selfmsgService()
#         self.editprofile_service = editProfileService()
#         self.editpetname_service = editPetnameService()
#         self.editheadimg_service = editImgService()
#
#     def teardown_class(self):
#         UtilsDriver.quit_au_driver()
#
#     def test_moduser(self):
#         self.nav_service.intent_selfspace()
#         self.selfspace_service.intent_garden()
#         # time.sleep(3)
#         # self.selfgarden_service.scroll_page()
#         # time.sleep(3)
#         self.selfgarden_service.intent_selfmsg()
#         self.selfmsg_service.intent_headimg()
#         self.editheadimg_service.modImgMsg()
#         self.selfmsg_service.intent_petname()
#         self.editpetname_service.modPetname("chasonche")
#         self.selfmsg_service.intent_profile()
#         self.editprofile_service.modProfileMsg("ooooooooo")
#         self.selfmsg_service.selfmsgHandle.selfmsgObj.get_element()
#
