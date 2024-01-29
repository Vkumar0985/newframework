import time

import pytest

from generic.base_setup import Base_SetUp
from pom.OrderManagement_Page import OrderCreationPage
from generic.excel import Excel
# from scripts.test_valid_login import Test_ValidLogin


class Test_Create_Order(Base_SetUp):

    # @pytest.mark.run(order=1)
    def test_creating_order(self):
        reg_id = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 1)
        site_no = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 2)
        ware_house_code = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 3)
        req_point_code = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 4)
        req_point_name = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 5)
        district_code = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 6)
        depot_reference = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 7)
        item_code = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 8)

        # 1.login to the application
        #login_to_saas = Test_ValidLogin()
        #login_to_saas.test_valid_login()

        # 2. Creating an order
        ocp = OrderCreationPage(self.driver)
        ocp.click_order_management()
        time.sleep(5)
        op_status = ocp.verify_create_order_page_displayed(self.wait)
        assert op_status
        time.sleep(5)
        ocp.click_create_order()
        time.sleep(5)
        ocp.click_drop_down()
        ocp.click_search_link()
        ocp.set_reg_id(reg_id)
        # ocp.click_reg_id_sel()
        ocp.search_btn()
        ocp.ok_btn_sel()
        time.sleep(5)
        # ocp.bill_to_drop_down()
        # ocp.bill_to_acc_sel()
        ocp.ship_to_dropdown_click()
        ocp.ship_to_search_link()
        time.sleep(5)
        ocp.set_site_no(site_no)
        ocp.ship_to_search_click()
        # ocp.site_no_click()
        ocp.site_no_ok()
        ocp.action_click()
        ocp.edit_info_click()
        time.sleep(5)
        ocp.set_ware_house_code(ware_house_code)
        ocp.set_req_point_code(req_point_code)
        ocp.set_req_point_name(req_point_name)
        ocp.set_district_code(district_code)
        ocp.set_depot_reference(depot_reference)
        ocp.add_info_ok_click()
        time.sleep(5)
        ocp.set_item_code(item_code)
        time.sleep(15)
        add_btn_display = ocp.verify_add_btn_is_displayed(self.wait)
        assert add_btn_display
        ocp.set_qty(qty="5")
        ocp.click_add_line()
        time.sleep(5)
        item_added = ocp.verify_item_is_added(self.wait)
        assert item_added
        ocp.click_submit()
        item_created = ocp.verify_sales_order_created(self.wait)
        assert item_created
