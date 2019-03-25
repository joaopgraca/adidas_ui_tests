# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re


class SearchKeyword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.adidas.fi/")


        try:
            element = driver.find_elements_by_class_name("gl-modal__main");
            driver.find_element_by_css_selector("button.gl-modal__close > svg.gl-icon").click()
            print("Pop up found")
        except NoSuchElementException:
            print("No pop up found")

        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("boost")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
