from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from generic.excel import Excel


class OrderValidationPage:
    __OrderManagement = (By.XPATH, "//a[@id='itemNode_order_management_order_management_0']")
    __Create_order_page = (By.XPATH, "//*[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:0:AP1:ip2:cpd:grpsdu:dc_ddc1:ddc_pgl1']")
    __advanced_lnk = (By.XPATH, "//a[text()='Advanced']")
    __source_order = (By.XPATH, "//input[@aria-label=' Source Order']")
    __cust_reg = (By.XPATH, "//input[@aria-label=' Customer Registry ID']")
    __search_btn_click = (By.XPATH, "//button[text()='Sea' and text()='ch']")
    __order_status = (By.XPATH, "//span[text()='Awaiting Shipping']")
    __actions_click = (By.XPATH, "//td/a[text()='Actions']")
    __switch_to_fulfillment = (By.XPATH, "//td[text()='Switch to Fulfillment View']")
    __fulfillment_lines = (By.XPATH, "//a[text()='Fulfillment Lines']")
    __supply_details = (By.XPATH, "//a[text()='Supply Details']")
    __purchase_order = (By.XPATH, "//*[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:3:OrderDAP:DooFu1:0:DooAt1:0:Supply:0"
                                  ":plam20']/td[2]")
    __promised_ship_date = (By.XPATH, "//*[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:3:OrderDAP:DooFu1:0:DooAt1:0:Supply:0"
                                      ":plam11']/td[2]")
    __supplier_details = (By.XPATH, "//*[@id='pt1:_FOr1:1:_FONSr2:0:_FOTsr1:3:OrderDAP:DooFu1:0:DooAt1:0:Supply:0"
                                    ":plam33']/td[2]")
    __Refresh_btn = (By.XPATH, "//button[text()='Refresh']")
    __done_click = (By.XPATH, "//span[@class='x1k8']")
    __home_click = (By.XPATH, "//a[@id='pt1:_UIShome']//*[name()='svg']//*[name()='g']//*[name()='path' and contains(@class,'svg-outlin')]")



    def __init__(self, driver):
        self.driver = driver

    def click_order_management(self):
        self.driver.find_element(*self.__OrderManagement).click()

    def verify_search_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__Create_order_page))
            print("Order search page is displayed")
            return True
        except:
            print("order search page is not displayed")
            return False

    def click_advance_link(self):
        self.driver.find_element(*self.__advanced_lnk).click()

    def set_source_order(self, source_order):
        self.driver.find_element(*self.__source_order).send_keys(source_order)

    def set_customer_reg(self, reg_id):
        self.driver.find_element(*self.__cust_reg).send_keys(reg_id)

    def click_search_btn(self):
        self.driver.find_element(*self.__search_btn_click).click()

    def verify_order_status(self):
        element = self.driver.find_element(*self.__order_status)
        while not element.is_displayed():
            self.driver.find_element(*self.__Refresh_btn).click()
            if element.is_displayed():
                break
            print("order status displayed")

    def action_click(self):
        self.driver.find_element(*self.__actions_click).click()

    def switch_to_click(self):
        self.driver.find_element(*self.__switch_to_fulfillment).click()

    def fulfillment_link_click(self):
        self.driver.find_element(*self.__fulfillment_lines).click()

    def supply_details_click(self):
        self.driver.find_element(*self.__supply_details).click()

    def verify_purchase_created(self):
        global PO
        try:
            purchase_order = self.driver.find_element(*self.__purchase_order)
            PO=purchase_order.text
            if PO != "":
                print("Purchase order generated: ", PO)
                Excel.write_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 11, PO)
                return True
        except Exception as e:
                print("Purchase order generated: ", e)
                return False

    def verify_Supply_details_displayed(self):
        try:
            supplier_details = self.driver.find_element(*self.__supplier_details)
            SD=supplier_details.text
            if SD is not None:
                print("supplier details displayed: ", SD)
                Excel.write_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 12, SD)
                return True
        except Exception as e:
                print("supplier details not displayed: ",e)
                return False

    def verify_Promised_ship_date_displayed(self):
        try:
            promised_ship_date = self.driver.find_element(*self.__promised_ship_date)
            PSD=promised_ship_date.text
            if PSD is not None:
                print("Promised ship date displayed: ", PSD)
                Excel.write_cell_data("../test_data/DOH_Test_Data.xlsx", "CreateOrder", 2, 13, PSD)
                return True
        except Exception as e:
                print("Promised ship date not displayed: ", e)
                return False

    def click_done(self):
        self.driver.find_element(*self.__done_click).click()

    def click_home(self):
        self.driver.find_element(*self.__home_click).click()
