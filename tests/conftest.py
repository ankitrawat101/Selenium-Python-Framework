import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver: webdriver.Remote


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    global driver

    if browser_name == "chrome":
        service = Service(executable_path="D:\\Web drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser_name == "firefox":
        service = Service(executable_path="D:\\Web drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser_name == "edge":
        service = Service(executable_path="D:\\Web drivers\\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)

    driver.get("https://www.google.com")

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
