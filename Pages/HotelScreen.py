from Pages.BasePage import BasePage


class Hotelscreen (BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def searchHotel(self,city):
        self.click("destination_XPATH")
        self.type("searchtext_XPATH",city)
        self.click("selectlocation_XPATH")
        self.click("searchbtn_XPATH")