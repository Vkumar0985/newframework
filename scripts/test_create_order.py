import time

import pytest

from generic.base_setup import Base_SetUp
from pom.OrderCreation_Page import OrderCreationPage
from generic.excel import Excel
from pom.login_page import LoginPage


class Test_Create_Order(Base_SetUp):

    # @pytest.mark.run(order=1)
    def test_creating_order(self):
        reg_id = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 1)
        site_no = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 2)
        ware_house_code = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 3)
        req_point_code = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 4)
        req_point_name = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 5)
        district_code = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 6)
        depot_reference = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 7)
        item_code = Excel.get_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 8)

        # 1.login to the application
        #login_to_saas = Test_ValidLogin(self)
        #login_to_saas.test_valid_login()

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

        # 2. Creating an order
        ocp = OrderCreationPage(self.driver)
        ocp.click_order_management()
        time.sleep(5)
        op_status = ocp.verify_create_order_page_displayed(self.wait)
        assert op_status
        time.sleep(5)
        ocp.click_create_order()
        time.sleep(10)
        ocp.click_drop_down()
        ocp.click_search_link()
        ocp.set_reg_id(reg_id)
        # ocp.click_reg_id_sel()
        ocp.search_btn()
        ocp.ok_btn_sel()
        time.sleep(10)
        # ocp.bill_to_drop_down()
        # ocp.bill_to_acc_sel()
        ocp.ship_to_dropdown_click()
        ocp.ship_to_search_link()
        time.sleep(5)
        ocp.set_site_no(site_no)
        ocp.ship_to_search_click()
        # ocp.site_no_click()
        ocp.site_no_ok()
        time.sleep(5)
        ocp.action_click()
        ocp.edit_info_click()
        time.sleep(5)
        ocp.set_ware_house_code(ware_house_code)
        time.sleep(5)
        ocp.set_req_point_code(req_point_code)
        ocp.set_req_point_name(req_point_name)
        ocp.set_district_code(district_code)
        time.sleep(5)
        ocp.set_depot_reference(depot_reference)
        time.sleep(5)
        ocp.add_info_ok_click()
        time.sleep(5)
        ocp.set_item_code(item_code)
        time.sleep(15)
        add_btn_display = ocp.verify_add_btn_is_displayed(self.wait)
        assert add_btn_display
        ocp.set_qty(qty="5")
        ocp.click_add_line()
        time.sleep(10)
        item_added = ocp.verify_item_is_added(self.wait)
        assert item_added
        ocp.click_submit()
        item_created = ocp.verify_sales_order_created(self.wait)
        assert item_created
        time.sleep(5)
        ocp.click_Ok_submit()
