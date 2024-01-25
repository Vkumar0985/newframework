import time

import pytest

from generic.base_setup import Base_SetUp
from pom.login_page import LoginPage
from generic.excel import Excel
from pom.logout_page import LogoutPage


class Test_ValidLogin(Base_SetUp):

    # @pytest.mark.run(order=1)
    def test_valid_login(self):
        un = Excel.get_cell_data("../test_data/input.xlsx", "validlogin", 2, 1)
        pw = Excel.get_cell_data("../test_data/input.xlsx", "validlogin", 2, 2)
        # 1. Enter Valid UN
        login_page = LoginPage(self.driver)
        # self.driver.implicitly_wait(10)
        login_status = login_page.verify_login_page_displayed(self.wait)
        assert login_status
        login_page.set_username(un)
        print("Entered the username:", un)
        # 2. Enter Valid PW
        login_page.set_password(pw)
        print("Entered the Password:", pw)
        # 3. Click on login Button
        login_page.click_signin_button()
        time.sleep(5)
        login_page.click_link()
        time.sleep(15)
        # 4. Verify that Home page is Displayed
        # homepage = LoginPage(self.driver)
        status = login_page.verify_homepage_displayed(self.wait)
        assert status

