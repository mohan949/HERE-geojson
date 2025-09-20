import pytest
from playwright.sync_api import sync_playwright

from geojson_tests.pages.geojson_page import GeoJSONPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser with a visible window (default: headless)",
    )


@pytest.fixture
def page(request):
    headed = request.config.getoption("--headed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture
def geojson_page(page):
    return GeoJSONPage(page)
