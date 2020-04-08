from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen


class AosPrivatePolicyStatementsScreen(BaseScreen):
    AGREE_BUTTON = (By.ID, 'btn_agree')

    def wait_page(self):
        return self.action_helper.wait_until_text_to_be_present_in_element('txt_title', 'Privacy Policy Statements')

    def click_agree_button(self):
        self.driver.find_element(*self.AGREE_BUTTON).click()


# TODO: Not implemented yet
class IosPrivatePolicyStatementsScreen(BaseScreen):
    AGREE_BUTTON = (By.ID, 'btn_agree')
