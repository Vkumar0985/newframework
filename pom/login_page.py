from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LoginPage:
    __username = (By.ID, "userid")
    __password = (By.NAME, "password")
    __signin = (By.XPATH, "//button[@type='submit']")
    __homepage = (By.XPATH, "//a[@id='pt1:_UIScil1u']")
    __link = (By.XPATH, "//a[contains(text(),'have')]")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_signin_button(self):
        self.driver.find_element(*self.__signin).click()

    def click_link(self):
        self.driver.find_element(*self.__link).click()

    def verify_homepage_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__homepage))
            print("Home page is displayed")
            return True
        except:
            print("Home page is NOT displayed")
            return False

    def verify_login_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__username))
            print("login Page is displayed")
            return True
        except:
            print("login Page is NOT displayed")
            return False
