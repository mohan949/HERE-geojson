import pytest
from playwright.sync_api import sync_playwright

from geojson_tests.pages.geojson_page import GeoJSONPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser with a visible window (default: headless)",
    )
    parser.addoption(
        "--slowmo",
        action="store",
        type=int,
        default=0,
        help="Delay Playwright actions in milliseconds",
    )


@pytest.fixture
def page(request):
    headed = request.config.getoption("--headed")
    slow_mo = request.config.getoption("--slowmo")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed, slow_mo=slow_mo)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield page
        finally:
            context.close()
            browser.close()


@pytest.fixture
def geojson_page(page):
    return GeoJSONPage(page)
