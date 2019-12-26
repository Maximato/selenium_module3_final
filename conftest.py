import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Select language: default 'ru'")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")

    # get user language from command line
    user_language = request.config.getoption("language")

    # create options
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # run browser
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)

    yield browser
    print("\nquit browser..")
    browser.quit()
