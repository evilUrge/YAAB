import logging
import unittest
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.user_search_utils import UserSearchUtils
from utils.consts import BASE_PATH
from utils.common import EC2Utils


class TestSuiteBase(unittest.TestCase):
    """
    Wrapper class for Selenium webdriver.
    Scalable for adding tests and a great cornerstone for automation infra.
    """

    @classmethod
    def create_driver(cls, agent):
        """
        Selenium webdriver creator.
        Please note that if the env is linux, than driver will be created locally in selenium grid server.
        Change this for a mobilefarm.

        :param agent: Agent is representing any browser params that is needed before running tests.

        :return: webdriver obj
        """
        capabilities = webdriver.ChromeOptions()
        if agent:
            capabilities.add_argument("--user-agent={}".format(agent))
        capabilities.add_argument('--unlimited-storage')

        if platform == 'linux2' and EC2Utils().is_ec:
            driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities=capabilities.to_capabilities())
        else:
            driver = webdriver.Chrome(executable_path='{base}utils/driver/{os}'.format(base=BASE_PATH, os=platform),
                                      chrome_options=capabilities)
        driver.maximize_window()
        return driver

    def driver_wait(self, selector, find_element_by=By.CSS_SELECTOR, timeout=60,
                    locator=EC.visibility_of_element_located, invisibility=False):
        """
        a simpler driver_wait representative.
        :param selector:
        :param find_element_by: default CSS.
        :param timeout:
        :param locator:
        :param invisibility:
        :return: will freeze test until element was found. If timeout has reached return False.
        """
        if invisibility:
            locator = EC.invisibility_of_element_located
        return WebDriverWait(self.driver, timeout).until(locator((find_element_by, selector)))

    def document_query_selector(self, element, click=False, value=False):
        """
        In case selenium failed to catch elements (happens usually with Ajax elements), you can use this dumb
        query selector.

        :param element: CSS Selector type element.
        :param click: if True, element will be clicked.
        :param value: if True, will change the element value to value.
        :return: Because of JS limitations, this will return nothing; But the req will be executed!
        """
        return self.driver.execute_script(
            "document.querySelector('{ELEMENT}'){CLICK}{VALUE}".format(ELEMENT=element,
                                                                       CLICK='.click()' if click else '',
                                                                       VALUE='.value' if value else ''))

    @classmethod
    def setUp(cls, agent=False):
        LOGGER.setLevel(logging.WARNING)
        cls.driver = cls.create_driver(agent=agent)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


class SearchTestCase(TestSuiteBase):
    """
    demo interface.
    """
    def setUp(self):
        super(SearchTestCase, self).setUp()
        self.search_utils = UserSearchUtils(self)

    def tearDown(self):
        self.search_utils.clear_session()
        super(SearchTestCase, self).tearDown()
