from Pages.BasePage import BasePage


class VillasScreen(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def searchVilla(self,city):
        self.click("area_XPATH")
        self.type("searchtext_XPATH",city)
        self.click("selectlocation_XPATH")
        self.click("SelectDate_XPATH")
        self.click("fromDate_XPATH")
        self.click("toDate_XPATH")
        self.click("continue_XPATH")
        self.click("viewstays_XPATH")





        # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Hotels']").click()
        # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Search Anywhere']").click()
        # driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="edtSearch"]').send_keys("Delhi")
        # driver.find_element(AppiumBy.XPATH,
        #                     '//android.view.View[@resource-id="lytLocationItem"]/android.widget.Button').click()
        #
        # driver.find_element(AppiumBy.XPATH,
        #                     '//android.view.View[@resource-id="landing_main_search_date_lyt"]/android.widget.Button').click()
        # driver.find_element(AppiumBy.XPATH,
        #                     "(//android.view.ViewGroup[@resource-id='com.goibibo:id/parentDay'])[21]").click()
        # driver.find_element(AppiumBy.XPATH,
        #                     "(//android.view.ViewGroup[@resource-id='com.goibibo:id/parentDay'])[26]").click()
        # driver.find_element(AppiumBy.XPATH,
        #                     "//android.widget.Button[@resource-id='com.goibibo:id/btnCalendar']").click()
        #
        # driver.find_element(AppiumBy.XPATH,
        #                     "//android.view.View[@resource-id = 'hotel_landing_search_button'] / android.widget.Button").click()
        #
        # print(driver.page_source)
        # ScrollUtil.scroll_until_text_found(driver, "Virohaa", max_scrolls=10)