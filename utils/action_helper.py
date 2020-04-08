from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ActionHelper:

    def __init__(self, driver, wait_time):
        self.driver = driver
        self.wait_time = wait_time

    def wait_until_text_to_be_present_in_element(self, element_id, text):
        return WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.text_to_be_present_in_element((By.ID, element_id), text))

    def wait_element_by_id(self, id):
        return WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located((By.ID, id)))

    def wait_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))