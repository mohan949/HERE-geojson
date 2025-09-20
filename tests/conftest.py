from pathlib import Path
import sys

import pytest
from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from geojson_tests.pages.geojson_page import GeoJSONPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store",
        nargs="?",
        const="true",
        default="false",
        help="Run browser with a visible window (accepts true/false, default false)",
    )


@pytest.fixture
def page(request):
    headed = _resolve_headed_flag(request.config.getoption("--headed"))
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


def _resolve_headed_flag(raw_value):
    if isinstance(raw_value, bool):
        return raw_value
    normalized = str(raw_value).strip().lower()
    return normalized in {"true", "1", "yes", "on"}
