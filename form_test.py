import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class HTMLTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 

    def tearDown(self):
        self.driver.quit()

    def test_validateTestCase_valid1(self):
        """
        Test Case 1 - Valid Input

        The piles are [3, 6, 7, 11], and the maximum number of hours available is 8.
        The expected minimum eating speed is 4.
        This test case verifies that the HTML form validation returns the correct result for a valid input.
        """
        self.driver.get('file:///form.html')

        piles_field = self.driver.find_element_by_id('pilesField')
        hours_field = self.driver.find_element_by_id('hoursField')
        expected_field = self.driver.find_element_by_id('expectedField')
        validate_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Validate')]")
        validation_result = self.driver.find_element_by_id('validationResult')

        piles_field.send_keys('3,6,7,11')
        hours_field.send_keys('8')
        expected_field.send_keys('4')
        validate_button.click()

        result_text = validation_result.text.strip()
        self.assertTrue(result_text == 'Valid test case. Result matches expected value.')
        self.assertTrue(validation_result.value_of_css_property('color') == 'rgba(0, 128, 0, 1)')

    def test_validateTestCase_invalid1(self):
        """
        Test Case 2 - Invalid Input

        The piles are [5, 10, 15, 20], and the maximum number of hours available is 100.
        This test case verifies that the HTML form validation returns the correct result for an invalid input.
        """
        self.driver.get('file:///form.html')

        piles_field = self.driver.find_element_by_id('pilesField')
        hours_field = self.driver.find_element_by_id('hoursField')
        expected_field = self.driver.find_element_by_id('expectedField')
        validate_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Validate')]")
        validation_result = self.driver.find_element_by_id('validationResult')

        piles_field.send_keys('5,10,15,20')
        hours_field.send_keys('100')
        expected_field.send_keys('0')
        validate_button.click()

        result_text = validation_result.text.strip()
        self.assertFalse(result_text == 'Invalid test case. Please enter valid numeric values.')
        self.assertFalse(validation_result.value_of_css_property('color') == 'rgba(255, 0, 0, 1)')

if __name__ == '__main__':
    unittest.main()
