from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen


class AosWeatherForecastScreen(BaseScreen):
    def wait_page(self):
        return self.action_helper.wait_element_by_xpath('//android.widget.TextView[@text="Weather Forecast"]')

    def scroll_to_day(self, day):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable('
                                                        'true).instance(2)).scrollIntoView(new UiSelector('
                                                        ').description("' + day + '").instance(0))')

    def is_forecast_weather_displayed(self, day):
        return self.driver.find_element(*(By.XPATH, '//android.widget.TextView[@content-desc="' + day + '"]'))


# TODO: Not implemented yet
class IosWeatherForecastScreen(BaseScreen):
    AGREE_BUTTON = (By.ID, 'btn_agree')
