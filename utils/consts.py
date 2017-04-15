# -*- coding: utf-8 -*-

"""
Main usage of consts is for common used strings.
Each class representing a page as part of an entire flow.
"""

import os

BASE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..')) + os.path.sep

BASE_URL = 'https://duckduckgo.com'


BROWSER_AGENT = {
    'IOS': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
    'ANDROID': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
}


class LoginCredentials(object):
    STUB_USERNAME = 'Demo'
    STUB_PASSWORD = 'Demo'


class SearchPage(object):
    SEARCH_TEXT_BOX = '#search_form_input'
    SEARCH_BUTTON = '#search_button'

    SEARCH_TEXT_BOX_HOMEPAGE = SEARCH_TEXT_BOX + '_homepage'
    SEARCH_BUTTON_HOMEPAGE = SEARCH_BUTTON + '_homepage'

    RESULTS_TITLE_TEXT_LIST = '.result__title'
    RESULTS_BODY_TEXT_LIST = 'div.result__snippet'
    RESULTS_URL_TEXT_LIST = '.result__url__domain'
