from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class GoogleHomePage(PageFactory):
    # searchField = (By.XPATH, "//textarea[@title='Search']")
    # searchButton = (By.XPATH, "//input[@aria-label='Google Search']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "searchField": ("XPATH", "//textarea[@title='Search']"),
        "searchButton": ("XPATH", "//input[@aria-label='Google Search']")
    }

    def enter_search_query(self, query):
        self.searchField.set_text(query)
        # self.driver.find_element(*GoogleHomePage.searchField).send_keys(query)

    def click_on_search_btn(self):
        self.searchButton.click()
        # self.driver.find_element(*GoogleHomePage.searchButton).click()
