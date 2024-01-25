import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties


class Base_SetUp:
    CONFIG_PATH = "../config.properties"
    XL_PATH = "../test_data/input.xlsx"

    @pytest.fixture(autouse=True)
    def precondition(self):
        ppt_obj = Properties()
        ppt_obj.load(open(self.CONFIG_PATH))
        grid = ppt_obj["GRID"]
        grid_url = ppt_obj["GRID_URL"]
        browser = ppt_obj["BROWSER"]
        ito = ppt_obj["ITO"]
        eto = ppt_obj["ETO"]
        app_url = ppt_obj["APP_URL"]

        if grid.lower() == "yes":
            print("Execute script on Remote System")
            if browser.lower() == "chrome":
                options = ChromeOptions()
            elif browser.lower() == "firefox":
                options = FirefoxOptions()
            else:
                options = EdgeOptions()

            print("Open the browser:", browser)
            self.driver = Remote(command_executor=grid_url, options=options)

        else:
            print("Execute script on Local System")
            print("Open the browser:", browser)
            if browser.lower() == "chrome":
                self.driver = Chrome()
            elif browser.lower() == "firefox":
                self.driver = Firefox()
            else:
                self.driver = Edge()

        print("Set ITO:", ito, "seconds")
        self.driver.implicitly_wait(ito)
        print("Set ETO:", eto, "seconds")
        self.wait = WebDriverWait(self.driver, eto)
        print("Maximize the window")
        self.driver.maximize_window()
        print("Enter the URL:", app_url)
        self.driver.get(app_url)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.close()
