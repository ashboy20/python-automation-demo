from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen


class AosHomeScreen(BaseScreen):
    NAVIGATE_UP_BUTTON = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    def wait_page(self):
        return self.action_helper.wait_element_by_xpath('//android.widget.TextView[@text="MyObservatory"]')

    def click_navigate_up_button(self):
        navigate_up_button = self.driver.find_element(*self.NAVIGATE_UP_BUTTON)
        navigate_up_button.click()

    def click_item_from_left_drawer(self, item):
        item = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable('
                                                               'true).instance(0)).scrollIntoView(new UiSelector('
                                                               ').text("' + item + '").instance(0))')
        item.click()


# TODO: Not implemented yet
class IosHomeScreen(BaseScreen):
    AGREE_BUTTON = (By.ID, 'btn_agree')
