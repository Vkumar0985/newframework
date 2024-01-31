import time

import pytest
from selenium.webdriver.common.by import By

from generic.base_setup import Base_SetUp
from generic.excel import Excel
from pom.OrderValidation_Page import OrderValidationPage
from pom.login_page import LoginPage


class Test_Validate_Order(Base_SetUp):

    # @pytest.mark.run(order=1)
    def test_validate_order(self):
        reg_id = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 1)
        source_order = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 10)
        un = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "Login", 2, 1)
        pw = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "Login", 2, 2)
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

        # 2. validating  an order
        ovp = OrderValidationPage(self.driver)
        ovp.click_order_management()
        time.sleep(5)
        op_status = ovp.verify_search_page_displayed(self.wait)
        assert op_status
        time.sleep(5)
        ovp.click_advance_link()
        ovp.set_source_order(source_order)
        ovp.set_customer_reg(reg_id)
        ovp.click_search_btn()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[text()='" + source_order + "']").click()
        time.sleep(5)
        ovp.verify_order_status()
        ovp.action_click()
        time.sleep(3)
        ovp.switch_to_click()
        time.sleep(3)
        ovp.fulfillment_link_click()
        time.sleep(3)
        ovp.supply_details_click()
        time.sleep(3)
        po_status = ovp.verify_purchase_created()
        assert po_status
        psd_status = ovp.verify_Promised_ship_date_displayed()
        assert psd_status
        sd_status = ovp.verify_Supply_details_displayed()
        assert sd_status
        time.sleep(5)
        ovp.click_done()
        time.sleep(5)
        ovp.click_home()
