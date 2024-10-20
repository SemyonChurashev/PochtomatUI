from playwright.sync_api import Page
from pathlib import Path


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://website.dev2.pochtomat.team"

    def open_page(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("load")

    def make_screenshot(self, device_name):
        path = f'{Path('..')}/tmp/{device_name}_screenshot.png'
        self.page.screenshot(path=path)


