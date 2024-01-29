from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from generic.excel import Excel


class OrderCreationPage:
    __bill_to = Excel.get_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 9)
    __signin = (By.XPATH, "//button[@type='submit']")
    __OrderManagement = (By.XPATH, "//a[@id='itemNode_order_management_order_management_0']")
    __Create_order_page = (By.XPATH, "//*[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:0:AP1:ip2:cpd:grpsdu:dc_ddc1:ddc_pgl1']")
    __create_order = (By.XPATH, "//div[contains(@id,'AP1:createbtn')]")
    __drop_down = (By.XPATH, "//span/a[@title='Search: Customer']")
    __search_click = (By.XPATH, "//a[contains(text(),'Search.')]")
    __reg_id = (By.XPATH, "//input[@aria-label=' Registry ID']")
    __search_btn = (By.XPATH, "//button[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:1:AP1:qryId1::search']")
    __reg_id_sel = (By.XPATH, "//td/span[text()='+reg_id+']")
    __ok_sel = (By.XPATH, "//button[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:1:AP1:partyNameId::lovDialogId::ok']")
    __bill_to_drop_down = (By.XPATH, "//a[contains(@id,'AP1:billToCustomerId::lovIconId']")
    __bill_to_acc = (By.XPATH, "//td/span[contains(text(),'+bill_to+')]")
    __ship_to_dropdown = (By.XPATH, "//a[@title='Search: Ship-to Address']")
    __ship_to_search = (By.XPATH, "//a[contains(text(),'Search.')]")
    __site_no = (By.XPATH, "//input[@aria-label=' Site Number']")
    __site_search = (By.XPATH, "//button[text()='Search']")
    __site_no_click = (By.XPATH, "//span[text()='+site_no+']")
    __site_no_ok = (By.XPATH, "//button[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:1:AP1:shipToAddress::lovDialogId::ok']")
    __actions_click = (By.XPATH, "//td/a[text()='Actions']")
    __edit_add_info = (By.XPATH, "//td[text()='Edit Additional Information']")
    __ware_house_code = (By.XPATH, "//input[contains(@id,'warehouseCode')]")
    __req_point_code = (By.XPATH, "//input[contains(@id,'requisitionPointCode')]")
    __req_point_name = (By.XPATH, "//input[contains(@id,'requisitionPointName')]")
    __district_code = (By.XPATH, "//input[contains(@id,'districtCode')]")
    __depot_reference = (By.XPATH, "//input[contains(@id,'depotReference')]")
    __add_info_ok = (By.XPATH, "//button[contains(@id,'1:AP1:dEffAttr::ok')]")
    __item_code = (By.XPATH, "//input[contains(@id,'AP1:itemNumberId2:lovTxtId::content')]")
    __set_qty = (By.XPATH, "//input[contains(@id,'createLineQuantity::content')]")
    __add_line = (By.XPATH, "//div[contains(@id,'AP1:addLine')]/a")
    __line_added = (By.XPATH, "//div[contains(@id,'AP1:pc1:ctb1')]/a")
    __submit = (By.XPATH, "//a/span[text() = 'Submit']")
    __Confirmation = (By.XPATH, "//td[contains(text(),'was submitted.')]")
    __Ok_Submit = (By.XPATH, "//button[@title='OK']")

    def __init__(self, driver):
        self.driver = driver

    def click_order_management(self):
        self.driver.find_element(*self.__OrderManagement).click()

    def verify_create_order_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__Create_order_page))
            print("Create Order page is displayed")
            return True
        except:
            print("Create order page is not displayed")
            return False

    def click_create_order(self):
        self.driver.find_element(*self.__create_order).click()

    def click_drop_down(self):
        self.driver.find_element(*self.__drop_down).click()

    def click_search_link(self):
        self.driver.find_element(*self.__search_click).click()

    def set_reg_id(self, reg_id):
        self.driver.find_element(*self.__reg_id).send_keys(reg_id)

    def click_reg_id_sel(self):
        self.driver.find_element(*self.__reg_id_sel).click()

    def search_btn(self):
        self.driver.find_element(*self.__search_btn).click()

    def ok_btn_sel(self):
        self.driver.find_element(*self.__ok_sel).click()

    def bill_to_drop_down(self):
        self.driver.find_element(*self.__bill_to_drop_down).click()

    def bill_to_acc_sel(self):
        self.driver.find_element(*self.__bill_to_acc).click()

    def ship_to_dropdown_click(self):
        self.driver.find_element(*self.__ship_to_dropdown).click()

    def ship_to_search_link(self):
        self.driver.find_element(*self.__ship_to_search).click()

    def set_site_no(self, site_no):
        self.driver.find_element(*self.__site_no).send_keys(site_no)

    def ship_to_search_click(self):
        self.driver.find_element(*self.__site_search).click()

    def site_no_click(self):
        self.driver.find_element(*self.__site_no_click).click()

    def site_no_ok(self):
        self.driver.find_element(*self.__site_no_ok).click()

    def action_click(self):
        self.driver.find_element(*self.__actions_click).click()

    def edit_info_click(self):
        self.driver.find_element(*self.__edit_add_info).click()

    def set_ware_house_code(self, ware_house_code):
        self.driver.find_element(*self.__ware_house_code).send_keys(ware_house_code)

    def set_req_point_code(self, req_point_code):
        self.driver.find_element(*self.__req_point_code).send_keys(req_point_code)

    def set_req_point_name(self, req_point_name):
        self.driver.find_element(*self.__req_point_name).send_keys(req_point_name)

    def set_district_code(self, district_code):
        self.driver.find_element(*self.__district_code).send_keys(district_code)

    def set_depot_reference(self, depot_reference):
        self.driver.find_element(*self.__depot_reference).send_keys(depot_reference)

    def add_info_ok_click(self):
        self.driver.find_element(*self.__add_info_ok).click()

    def set_item_code(self, item_code):
        self.driver.find_element(*self.__item_code).send_keys(item_code)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def verify_add_btn_is_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__set_qty))
            print("Add Page is displayed to enter the quantity")
            return True
        except:
            print("Add Page is not displayed")
            return False

    def set_qty(self, qty):
        self.driver.find_element(*self.__set_qty).send_keys(qty)

    def click_add_line(self):
        self.driver.find_element(*self.__add_line).click()

    def verify_item_is_added(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__line_added))
            print("Item added successfully ")
            return True
        except:
            print("item not added")
            return False

    def click_submit(self):
        self.driver.find_element(*self.__submit).click()

    def verify_sales_order_created(self, wait):
        global Sales_order
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__Confirmation))

            confirmation_msg = self.driver.find_element(*self.__Confirmation)
            sent = confirmation_msg.text
            res = sent.split()
            for i in res:
                if i.isnumeric():
                    Sales_order = i
            print("Sales order created successfully: " + Sales_order)
            Excel.write_cell_data("../test_data/input.xlsx", "CreateOrder", 2, 10, Sales_order)
            return True
        except:
            print("Sales order creation failed")
            return False

    def click_Ok_submit(self):
        self.driver.find_element(*self.__Ok_Submit).click()
