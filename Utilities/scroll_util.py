from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ScrollUtil:

    @staticmethod
    def scroll_to_text(driver, text, max_swipes=20):
        """
        Scrolls vertically until the text is found.
        Tries UiScrollable first, then fallback to manual swiping.
        """

        # --- TRY UISCROLLABLE FIRST ---
        try:
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                'new UiSelector().textContains("{}"))'.format(text)
            )
            element.click()
            return
        except Exception:
            pass  # Continue to fallback scrolling

        # --- FALLBACK MANUAL SWIPES ---
        size = driver.get_window_size()
        start_y = size["height"] * 0.7
        end_y = size["height"] * 0.3
        x = size["width"] * 0.5

        for _ in range(max_swipes):
            try:
                element = driver.find_element(AppiumBy.XPATH, f"//*[contains(@text,'{text}')]")
                element.click()
                return
            except NoSuchElementException:
                # do swipe
                driver.swipe(x, start_y, x, end_y, 600)

        raise TimeoutException(f"❌ Could not find text: {text} after {max_swipes} swipes")

