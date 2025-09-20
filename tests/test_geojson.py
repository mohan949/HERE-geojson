


import pytest


@pytest.mark.fast
def test_launch_geojson_io(geojson_page):
    geojson_page.open_geojson_io()
    print("✅ Launched geojson.io using POM")


@pytest.mark.fast
def test_search_mumbai(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.search_location("mumbai")
    print("✅ Searched for Mumbai location")


@pytest.mark.slow
def test_map_interactions(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.search_location("mumbai")
    geojson_page.click_map_position(440, 271)
    geojson_page.zoom_in()
    geojson_page.zoom_out()
    geojson_page.select_drawing_tool("point")
    geojson_page.select_drawing_tool("line")
    geojson_page.select_drawing_tool("polygon")
    print("✅ Tested map interactions")


@pytest.mark.slow
def test_file_operations(geojson_page):
    geojson_page.open_geojson_io()
    geojson_page.open_file_menu()
    geojson_page.save_file()
    geojson_page.create_new_file()
    print("✅ Tested file operations")
