from utils.base import SearchTestCase
from utils.consts import SearchPage


class TestSearchFlow(SearchTestCase):
    def test_search_happy_flow(self):
        self.driver.find_element_by_css_selector(SearchPage.SEARCH_TEXT_BOX_HOMEPAGE).send_keys('Hummus')
        self.driver.find_element_by_css_selector(SearchPage.SEARCH_BUTTON_HOMEPAGE).click()
        self.driver_wait(SearchPage.RESULTS_TITLE_TEXT_LIST)

        first_title = self.driver.find_element_by_css_selector(SearchPage.RESULTS_TITLE_TEXT_LIST).text
        self.assertTrue('hummus' in first_title.lower(),
                        'Failed to make an search "Happy flow" please refer to test logs for additional information.')
