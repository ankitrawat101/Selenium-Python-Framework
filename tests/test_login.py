import pytest

from pages.google_home_page import GoogleHomePage
from testdata.data_google_home_page import DataGoogleHomePage
from utilities.base_config_utils import BaseConfig


class TestLogin(BaseConfig):

    def test_e2e(self, setup, get_search_data):

        self.driver = setup
        log = self.logger_init()
        googlePage = GoogleHomePage(self.driver)
        googlePage.enter_search_query(get_search_data["firstData"])
        log.info("Entering name")
        googlePage.click_on_search_btn()
        log.info("Clicked on search button")
        self.driver.back()
        log.info("Going on previous page")
        self.driver.refresh()
        log.info("Refreshing page")

    @pytest.fixture(params=DataGoogleHomePage.home_page_data)
    def get_search_data(self, request):
        json_data = self.get_data_from_json(self.get_project_root() + "\\testdata\\Google Search Data.json")
        print(json_data)
        return request.param
