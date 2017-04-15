from utils.consts import BASE_URL, LoginCredentials, SearchPage


class UserSearchUtils:
    def __init__(self, test_case):
        self.test_case = test_case
        self.navigate_to_client_url()

    def navigate_to_client_url(self, url=''):
        self.test_case.driver.get('{base}{url}'.format(base=BASE_URL, url=url))
        self.test_case.driver_wait(SearchPage.SEARCH_TEXT_BOX_HOMEPAGE)

    def clear_session(self):
        self.test_case.driver.delete_all_cookies()

    def login(self, user=LoginCredentials.STUB_USERNAME, password=LoginCredentials.STUB_PASSWORD, submit=True):
        """
        Stub for login; in this a login scenario is being created once to easily do a login scenario for tests that
        requires that.
        :param user: Should have a default user
        :param password: same here
        :param submit:
        :return: True if login was successful
        """
        pass

    def element_list_lookup(self, selector, term):
        for result in self.test_case.driver.find_elements_by_css_selector(selector):
            if term in result.text.encode('utf-8'):
                return result
        return False
