from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LogoutPage:
    __btn = (By.XPATH, "//img[@id='pt1:_UIScmil2u']")
    __lnk = (By.XPATH, "//a[text()='Sign Out']")
    __confirm = (By.XPATH, "//button[@name='Confirm']")

    def __init__(self, driver):
        self.driver = driver

    def click_button(self):
        self.driver.find_element(*self.__btn).click()

    def click_link(self):
        self.driver.find_element(*self.__lnk).click()

    def verify_logout_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__confirm))
            print("Logout from the application is successful")
            return True
        except:
            print("Logout from the application unsuccessful")
            return False
