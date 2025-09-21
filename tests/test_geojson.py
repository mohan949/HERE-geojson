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
    for step in (
        geojson_page.zoom_in,
        geojson_page.zoom_out,
        lambda: geojson_page.select_drawing_tool("point"),
        lambda: geojson_page.select_drawing_tool("line"),
        lambda: geojson_page.select_drawing_tool("polygon"),
    ):
        geojson_page.page.wait_for_timeout(3000)
        step()
    assert geojson_page.is_tool_active("polygon")
    assert geojson_page.is_map_ready()

def test_file_operations(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.open_file_menu()
    assert geojson_page.is_file_menu_open()
    geojson_page.save_file()
    geojson_page.create_new_file()
