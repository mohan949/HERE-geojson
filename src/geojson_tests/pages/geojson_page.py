from playwright.sync_api import Page
from .base_page import BasePage


class GeoJSONPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "https://geojson.io/"
    
    def open_geojson_io(self):
        self.navigate_to(f"{self.base_url}#map=2/0/20")
        self.wait_for_text("geojson.io")
    
    def search_location(self, location):
        search_box = self.search_input()
        search_box.click()
        search_box.fill("")
        search_box.type(location, delay=80)
        suggestion = self.page.locator(".suggestions li").first
        suggestion.wait_for(state="visible")
        suggestion.locator("a").first.click()
        self.page.wait_for_timeout(3000)

    def search_input(self):
        return self.page.get_by_role("textbox", name="Search")
    
    def click_map_position(self, x, y):
        self.page.get_by_role("region", name="Map").click(position={"x": x, "y": y})
    
    def zoom_in(self):
        self.page.get_by_role("button", name="Zoom in").click()
    
    def zoom_out(self):
        self.page.get_by_role("button", name="Zoom out").click()
    
    def select_drawing_tool(self, tool):
        tool_config = self._drawing_tools().get(tool)
        if not tool_config:
            return
        self.page.get_by_role("button", name=tool_config["label"]).click()
        self.page.wait_for_function(
            "expected => window.api?.draw?.getMode && window.api.draw.getMode() === expected",
            arg=tool_config["mode"],
        )

    def is_tool_active(self, tool):
        tool_config = self._drawing_tools().get(tool)
        if not tool_config:
            return False
        current_mode = self.page.evaluate("() => window.api?.draw?.getMode && window.api.draw.getMode()")
        return current_mode == tool_config["mode"]

    def _drawing_tools(self):
        return {
            "point": {"label": "Draw Point (m)", "mode": "draw_point"},
            "line": {"label": "Draw LineString (l)", "mode": "draw_line_string"},
            "polygon": {"label": "Draw Polygon (p)", "mode": "draw_polygon"},
        }
    
    def open_file_menu(self):
        self.page.locator("a.parent", has_text="Open").click()
    
    def save_file(self):
        self.page.locator("a.parent", has_text="Save").click()
    
    def create_new_file(self):
        self.page.locator("a.parent", has_text="New").click()

    def is_map_ready(self):
        return self.page.get_by_role("region", name="Map").is_visible()

    def is_file_menu_open(self):
        return self.page.locator('input[type="file"]').count() > 0
