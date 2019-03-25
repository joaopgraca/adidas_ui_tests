''' NOTE: This test suite contains 2 passing tests and 2 failing tests. '''

import pytest
import unittest, time, re

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
from seleniumbase import BaseCase


class AdidasTestSuite(BaseCase):

    def test_1(self):
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

    def test_2(self):
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


    def test_3(self):
        driver = self.driver
        driver.get("https://www.adidas.fi/on/demandware.store/Sites-adidas-FI-Site/fi_FI/MyAccount-Register")
        time.sleep(5)

        iframes = driver.find_elements_by_tag_name('iframe')
        print("No of frames present in the web page are: ", len(iframes))

        driver.switch_to.frame(iframes[5])
        driver.find_element_by_class_name("call").click()

        driver.switch_to.parent_frame()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dwfrm_profile_customer_firstname')))

        driver.find_element_by_id("dwfrm_profile_customer_firstname").send_keys("Joao")
        driver.find_element_by_id("dwfrm_profile_customer_lastname").clear()
        driver.find_element_by_id("dwfrm_profile_customer_lastname").send_keys("Graca")
        driver.find_element_by_id("dwfrm_profile_customer_birthday_dayofmonth").send_keys("15")
        driver.find_element_by_id("dwfrm_profile_customer_birthday_month").send_keys("05")
        driver.find_element_by_id("dwfrm_profile_customer_birthday_year").send_keys("1990")
        driver.find_element_by_id("birthday-field-original").click()
        driver.find_element_by_name("dwfrm_profile_register").click()