import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose GUI for language tests')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("test run should contain language for test")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")
    result = webdriver.Chrome(options=options)
    result.implicitly_wait(5)

    yield result
    print("\nquit browser..")
    result.quit()
