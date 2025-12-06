
import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android",
        "appPackage": "com.goibibo",
        "appActivity": ".common.HomeActivity",
        "automationName": "UiAutomator2",
        "noRest": "True"
    }
    # global driver
    driver = webdriver.Remote(
        "http://127.0.0.1:4723", options=UiAutomator2Options().load_capabilities(desired_caps)
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)




    # if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
    #     try:
    #         allure.attach(
    #             appium_driver.get_screenshot_as_png(),
    #             name=request.node.name,
    #             attachment_type=AttachmentType.PNG,
    #         )
    #         print(f"Screenshot captured for failed test: {request.node.name}")
    #     except Exception as e:
    #         print(f"Could not capture screenshot: {e}")
