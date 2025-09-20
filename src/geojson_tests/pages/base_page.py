from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def get_title(self):
        return self.page.title()
    
    def get_url(self):
        return self.page.url
    
    def click_element(self, selector: str):
        self.page.locator(selector).first.click()
    
    def fill_input(self, selector: str, text: str):
        self.page.locator(selector).first.fill(text)
    
    def wait_for_text(self, text: str):
        self.page.wait_for_selector(f"text={text}")
