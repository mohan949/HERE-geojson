


def test_launch_geojson_io(geojson_page):
    """Just launch geojson.io URL using POM"""
    geojson_page.open_geojson_io()
    print("✅ Launched geojson.io using POM")


def test_search_mumbai(geojson_page):
    """Search for Mumbai location"""
    geojson_page.open_geojson_io()
    geojson_page.search_location("mumbai")
    print("✅ Searched for Mumbai location")


def test_map_interactions(geojson_page):
    """Test various map interactions"""
    geojson_page.open_geojson_io()
    
    # Search for Mumbai
    geojson_page.search_location("mumbai")
    
    # Click on map
    geojson_page.click_map_position(440, 271)
    
    # Test zoom controls
    geojson_page.zoom_in()
    geojson_page.zoom_out()
    geojson_page.reset_bearing()
    
    # Test drawing tools
    geojson_page.select_drawing_tool("point")
    geojson_page.select_drawing_tool("line")
    geojson_page.select_drawing_tool("polygon")
    
    print("✅ Tested map interactions")


def test_file_operations(geojson_page):
    """Test file operations"""
    geojson_page.open_geojson_io()
    
    # Test file menu
    geojson_page.open_file_menu()
    geojson_page.save_file()
    
    # Create new file (opens popup)
    with geojson_page.page.expect_popup() as page1_info:
        geojson_page.create_new_file()
    page1 = page1_info.value
    
    # Test map styles in popup
    geojson_page.change_map_style("satellite")
    geojson_page.change_map_style("light")
    geojson_page.change_map_style("dark")
    
    print("✅ Tested file operations")
