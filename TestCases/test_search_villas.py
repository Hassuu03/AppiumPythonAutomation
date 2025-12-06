import pytest

from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import Hotelscreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil


class Test_SearchVilla(BaseTest):

    @pytest.mark.parametrize("city,hotel", dataProvider.get_data("VillaTest"))
    def test_searchVilla(self, appium_driver, city,hotel):
        home = HomeScreen(appium_driver)
        home.gotoVillas().searchVilla(city)
        ScrollUtil.scroll_to_text(appium_driver, hotel)
