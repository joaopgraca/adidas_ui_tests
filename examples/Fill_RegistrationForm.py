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


class FillRegForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()

    def test_untitled_test_case(self):
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
        driver.find_element_by_id("dwfrm_profile_customer_birthday_dayofmonth").click()
        driver.find_element_by_id("dwfrm_profile_customer_birthday_dayofmonth").clear()
        driver.find_element_by_id("dwfrm_profile_customer_birthday_dayofmonth").send_keys("15")
        driver.find_element_by_id("dwfrm_profile_customer_birthday_month").click()
        driver.find_element_by_id("dwfrm_profile_customer_birthday_month").clear()
        driver.find_element_by_id("dwfrm_profile_customer_birthday_month").send_keys("05")
        driver.find_element_by_id("dwfrm_profile_customer_birthday_year").clear()
        driver.find_element_by_id("dwfrm_profile_customer_birthday_year").send_keys("1990")
        driver.find_element_by_id("birthday-field-original").click()
        driver.find_element_by_name("dwfrm_profile_register").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
