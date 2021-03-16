from locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class PurchaseDomain:
    def __init__(self, driver):
        self.driver = driver
        self.domain_seacrh_box = Locators.domain_seacrh_box
        self.enter_text = Locators.enter_text
        self.drop_downops = Locators.drop_downops
        self.selecting_the_tld = Locators.selecting_the_tld


    def enter_the_domain_name(self):
        global element
        element = self.driver.find_element_by_css_selector(self.domain_seacrh_box)
        element.send_keys(self.enter_text)
        element.send_keys(Keys.ENTER)









