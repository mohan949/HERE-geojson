from pathlib import Path
import re

import pytest
from playwright.sync_api import expect


@pytest.mark.ci_safe
def test_launch_geojson_io(geojson_page):
    geojson_page.open_geojson_io()
    expect(geojson_page.page).to_have_url(re.compile(r"geojson\.io"))
    expect(geojson_page.page).to_have_title(re.compile(r"geojson", re.I))


@pytest.mark.ci_safe
@pytest.mark.parametrize("city", ["Mumbai", "Delhi"])
def test_search_city(geojson_page, city):
    geojson_page.open_geojson_io()
    geojson_page.search_location(city)
    expect(geojson_page.search_input()).to_have_value(re.compile(city, re.I))


@pytest.mark.ci_safe
def test_map_interactions(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.search_location("Mumbai")
    geojson_page.click_map_position(440, 271)
    geojson_page.zoom_in()
    geojson_page.zoom_out()
    geojson_page.select_drawing_tool("point")
    geojson_page.select_drawing_tool("line")
    geojson_page.select_drawing_tool("polygon")
    assert geojson_page.is_tool_active("polygon")
    assert geojson_page.is_map_ready()

@pytest.mark.ci_safe
def test_file_operations(geojson_page):
    geojson_page.open_geojson_io()
    data_file = Path(__file__).parent / "sample_points.csv"
    with geojson_page.page.expect_file_chooser() as chooser:
        geojson_page.open_file_menu()
    chooser.value.set_files(str(data_file))
    expect(
        geojson_page.page.locator("div.content", has_text="Imported 2 features.")
    ).to_be_visible()
    geojson_page.page.get_by_role("button", name=" JSON").click()
    expect(geojson_page.page.get_by_text('"name": "Gateway of India"')).to_be_visible()
    expect(geojson_page.page.get_by_text('"name": "India Gate"')).to_be_visible()


@pytest.mark.ci_safe
def test_upload_invalid_file_shows_error(geojson_page):
    geojson_page.open_geojson_io()
    invalid_file = Path(__file__).parent / "map.geojson"
    with geojson_page.page.expect_file_chooser() as chooser:
        geojson_page.open_file_menu()
    chooser.value.set_files(str(invalid_file))
    expect(
        geojson_page.page.locator("div.content", has_text="Imported 0 features.")
    ).to_be_visible()
