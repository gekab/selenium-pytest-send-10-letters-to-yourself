import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://ukr.net", help="choose your browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    print("\nStart work browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.get(url)
    yield driver
    print("\nEnd work browser")
    driver.quit()
