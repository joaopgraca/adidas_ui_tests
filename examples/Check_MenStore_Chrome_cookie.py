# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import unittest, time, re

class CheckMenStoreWithoutCookieValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.adidas.fi/")
        driver.get_cookies()

        try:
            element = driver.find_elements_by_class_name("gl-modal__main");
            driver.find_element_by_css_selector("button.gl-modal__close > svg.gl-icon").click()
            print("Pop up found")
        except NoSuchElementException:
            print("No pop up found")


        self.element_to_hover = driver.find_element_by_xpath('//a[@manual_cm_sp="header-_-Men"]')
        self.hover = ActionChains(driver).move_to_element(self.element_to_hover)
        self.hover.perform()

        driver.find_element_by_xpath('//a[@manual_cm_sp="header-_-men-_-featured-_-new arrivals"]').click()


if __name__ == "__main__":
    unittest.main()
