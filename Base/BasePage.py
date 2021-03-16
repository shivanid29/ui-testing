import pytest
from selenium import webdriver


class Base:

    @pytest.fixture()
    def setup(self):
        print("initiating chrome driver")
        self.driver = webdriver.Chrome(executable_path="C:/WebDriver/chromedriver.exe")
        print("----------------")
        print("starting the test")
        self.driver.implicitly_wait(10)
        self.driver.get("https://bigrock.in")
        self.driver.maximize_window()

        yield
        self.driver.close()
