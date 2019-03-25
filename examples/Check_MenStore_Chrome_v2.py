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


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()

    def test_untitled_test_case(self):
        driver = self.driver
        driver.implicitly_wait(90)
        driver.get("https://www.adidas.fi/")



        try:
            element = driver.find_elements_by_class_name("gl-modal__main");
            driver.find_element_by_css_selector("button.gl-modal__close > svg.gl-icon").click()
            print("Pop up found")
        except NoSuchElementException:
            print("No pop up found")


        # try:
        #     WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
        #     alert = driver.switch_to.alert
        #     alert.accept()
        #     print("alert accepted")
        #
        # except TimeoutException:
        #     print("no alert")

        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Cookie Use")))
        #



        # driver.find_elements_by_xpath()


        self.element_to_hover = driver.find_element_by_xpath('//a[@manual_cm_sp="header-_-Men"]')
        self.hover = ActionChains(driver).move_to_element(self.element_to_hover)
        self.hover.perform()

        driver.find_element_by_xpath('//a[@manual_cm_sp="header-_-men-_-featured-_-new arrivals"]').click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
