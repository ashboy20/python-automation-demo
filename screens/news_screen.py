from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen


class AosNewsScreen(BaseScreen):
    SKIP_BUTTON = (By.ID, 'btn_friendly_reminder_skip')

    def wait_page(self):
        return self.action_helper.wait_element_by_id('whatsNewTitle')

    def click_next_button(self, times):
        skip_button = self.driver.find_element(*self.SKIP_BUTTON)
        for i in range(0, times):
            skip_button.click()


# TODO: Not implemented yet
class IosNewsScreen(BaseScreen):
    AGREE_BUTTON = (By.ID, 'btn_agree')
