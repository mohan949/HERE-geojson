from playwright.sync_api import Page
from .base_page import BasePage


class GeoJSONPage(BasePage):
    SEARCH_TEXTBOX = 'role="textbox" name="Search"'
    ZOOM_IN_BUTTON = 'role="button" name="Zoom in"'
    ZOOM_OUT_BUTTON = 'role="button" name="Zoom out"'
    DRAW_POINT_BUTTON = 'role="button" name="Draw Point (m)"'
    DRAW_LINE_BUTTON = 'role="button" name="Draw LineString (l)"'
    DRAW_POLYGON_BUTTON = 'role="button" name="Draw Polygon (p)"'
    OPEN_BUTTON = 'text="Open" exact=true'
    SAVE_BUTTON = 'a:has-text("Save")'
    NEW_BUTTON = 'text="New"'
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "https://geojson.io/"
    
    def open_geojson_io(self):
        self.navigate_to(f"{self.base_url}#map=2/0/20")
        self.wait_for_text("geojson.io")
    
    def search_location(self, location):
        self.click_element(self.SEARCH_TEXTBOX)
        self.fill_input(self.SEARCH_TEXTBOX, location)
        self.click_element(f'a:has-text("{location}")')
    
    def click_map_position(self, x, y):
        self.page.get_by_role("region", name="Map").click(position={"x": x, "y": y})
    
    def zoom_in(self):
        self.click_element(self.ZOOM_IN_BUTTON)
    
    def zoom_out(self):
        self.click_element(self.ZOOM_OUT_BUTTON)
    
    def select_drawing_tool(self, tool):
        tools = {
            "point": self.DRAW_POINT_BUTTON,
            "line": self.DRAW_LINE_BUTTON,
            "polygon": self.DRAW_POLYGON_BUTTON
        }
        if tool in tools:
            self.click_element(tools[tool])
    
    def open_file_menu(self):
        self.click_element(self.OPEN_BUTTON)
    
    def save_file(self):
        self.click_element(self.SAVE_BUTTON)
    
    def create_new_file(self):
        self.click_element(self.NEW_BUTTON)
