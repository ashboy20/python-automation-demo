import json

import pytest

from appium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers

from screens.disclaimer_screen import AosDisclaimerScreen, IosDisclaimerScreen
from screens.home_screen import AosHomeScreen, IosHomeScreen
from screens.news_screen import AosNewsScreen, IosNewsScreen
from screens.private_policy_statments_screen import AosPrivatePolicyStatementsScreen, IosPrivatePolicyStatementsScreen
from screens.weather_forecast import AosWeatherForecastScreen, IosWeatherForecastScreen

scenarios('../features/')

DEFAULT_WAIT_TIME = 10
SUPPORTED_PLATFORMS = ['aos', 'ios']


@pytest.fixture(scope='session')
def config():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    return data


@pytest.fixture(scope='session')
def conf_platform(config):
    if 'platform' not in config:
        raise Exception('The config file does not contain "platform"')
    elif config['platform'] not in SUPPORTED_PLATFORMS:
        raise Exception(f'"{config["platform"]}" is not a supported platform')
    return config['platform']


@pytest.fixture(scope='session')
def conf_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def driver(conf_platform, conf_wait_time):
    if conf_platform == 'aos':
        desired_capabilities = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '9.0',
            'automationName': 'UiAutomator2',
            'appPackage': 'hko.MyObservatory_v1_0',
            'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
            'autoGrantPermissions': 'true'
        }
    elif conf_platform == 'ios':
        # TODO: impossible to implement the IOS side because no APP or developer ID available
        desired_capabilities = {
            'platformName': 'iOS',
            'deviceName': 'iPhone XR',
            'platformVersion': '13.2',
            'automationName': 'XCUITest',
            'app': '',
            "xcodeOrgId": "",
            "xcodeSigningId": "",
            'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
            'autoGrantPermissions': 'true'
            }
    else:
        raise Exception(f'"{conf_platform}" is not a supported browser')

    driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_capabilities)
    driver.implicitly_wait(conf_wait_time)
    yield driver
    driver.quit()


# TODO: Could have done better here by using yield to create page instances to fixture instead of returning a list of
#  page objects, or implement a dependency injection tool to make it better.
@pytest.fixture
def screens(driver, conf_wait_time, conf_platform):
    if conf_platform == 'aos':
        screens = {
            'disclaimer': AosDisclaimerScreen(driver, conf_wait_time),
            'private_policy_statements': AosPrivatePolicyStatementsScreen(driver, conf_wait_time),
            'news': AosNewsScreen(driver, conf_wait_time),
            'home': AosHomeScreen(driver, conf_wait_time),
            'weather_forecast': AosWeatherForecastScreen(driver, conf_wait_time)
        }
    elif conf_platform == 'ios':
        screens = {
            'disclaimer': IosDisclaimerScreen(driver, conf_wait_time),
            'private_policy_statements': IosPrivatePolicyStatementsScreen(driver, conf_wait_time),
            'news': IosNewsScreen(driver, conf_wait_time),
            'home': IosHomeScreen(driver, conf_wait_time),
            'weather_forecast': IosWeatherForecastScreen(driver, conf_wait_time)
        }
    return screens

# Cucumber steps with page/screen methods
@given('the user is in Disclaimer screen')
def in_disclaimer_screen(screens):
    screens['disclaimer'].wait_page()


@when('the user clicks Agree button on disclaimer screen')
def click_agree_button_on_disclaimer_screen(screens):
    screens['disclaimer'].click_agree_button()


@when('the user is redirected to Privacy Policy Statements screen')
def redirected_to_privacy_policy_statements_screen(screens):
    assert screens['private_policy_statements'].wait_page()


@when('the user clicks Agree button on Privacy Policy Statements screen')
def click_agree_button_on_privacy_policy_statement_screen(screens):
    screens['private_policy_statements'].click_agree_button()


@when('the user is redirected to News screen')
def redirected_to_news_screen(screens):
    assert screens['news'].wait_page()


@when(parsers.parse('the user clicks Next button {times:d} times'))
def click_next_button(screens, times):
    screens['news'].click_next_button(times)


@when('the user is redirected to Home screen')
def redirected_to_home_screen(screens):
    assert screens['home'].wait_page()


@when('the user clicks Navigate Up Button')
def click_navigate_up_button(screens):
    screens['home'].click_navigate_up_button()


@when(parsers.parse('the user clicks "{item}" from Left Drawer'))
def click_item_from_left_drawer(screens, item):
    screens['home'].click_item_from_left_drawer(item)


@when('the user is redirected to Weather Forecast screen')
@then('the user is redirected to Weather Forecast screen')
def redirected_to_weather_forecast_screen(screens):
    screens['weather_forecast'].wait_page()


@when(parsers.parse('the user scrolls to next <day>'))
def scroll_to_day(screens, day):
    screens['weather_forecast'].scroll_to_day(day)


@then(parsers.parse('the user sees the forecast weather for <day>'))
def see_forecast_weather(screens, day):
    assert screens['weather_forecast'].is_forecast_weather_displayed(day)
