import time

import pytest

from generic.base_setup import Base_SetUp
from pom.logout_page import LogoutPage
from scripts.test_valid_login import Test_ValidLogin


class Test_ValidLogout(Base_SetUp):

    # @pytest.mark.run(order=1)
    def test_valid_logout(self):
        # . Verify whether you are able log out
        logout_page = LogoutPage(self.driver)
        logout_page.click_button()
        time.sleep(5)
        logout_page.click_link()
        time.sleep(5)
        logout_status = logout_page.verify_logout_displayed(self.wait)
        assert logout_status
