import logging
from appium.webdriver.common.appiumby import AppiumBy
from Utilities.LogUtil import logger
from Utilities import configReader

log = logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        value = configReader.readConfig("locators", locator)

        if locator.endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, value).click()
        elif locator.endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value).click()
        elif locator.endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, value).click()

        log.logger.info(f"Clicking on Element: {locator}")

    def type(self, locator, text):
        value = configReader.readConfig("locators", locator)

        if locator.endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, value).send_keys(text)
        elif locator.endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value).send_keys(text)
        elif locator.endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, value).send_keys(text)

        log.logger.info(f"Typing in Element: {locator} | Value entered: {text}")

    def getText(self, locator):
        value = configReader.readConfig("locators", locator)

        if locator.endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, value).text
        elif locator.endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value).text
        elif locator.endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID, value).text

        log.logger.info(f"Getting text from Element: {locator}")
        return text
