from utils.action_helper import ActionHelper


class BaseScreen:

    def __init__(self, driver, wait_time):
        self.driver = driver
        self.wait_time = wait_time
        self.action_helper = ActionHelper(driver, wait_time)
