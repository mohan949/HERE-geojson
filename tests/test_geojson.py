import pytest
import re

from playwright.sync_api import expect


@pytest.mark.fast
def test_launch_geojson_io(geojson_page):
    geojson_page.open_geojson_io()
    expect(geojson_page.page).to_have_url(re.compile(r"geojson\.io"))
    expect(geojson_page.page).to_have_title(re.compile(r"geojson", re.I))


@pytest.mark.fast
def test_search_mumbai(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.search_location("Mumbai")
    expect(geojson_page.search_input()).to_have_value(re.compile("Mumbai", re.I))
    geojson_page.wait_for_text("Mumbai")


@pytest.mark.slow
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


@pytest.mark.slow
def test_file_operations(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.open_file_menu()
    assert geojson_page.is_file_menu_open()
    geojson_page.save_file()
    geojson_page.create_new_file()
