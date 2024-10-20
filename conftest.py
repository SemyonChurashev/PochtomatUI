import pytest
from playwright.sync_api import sync_playwright

devices = [
    "iPhone 15 Pro Max",
    "Pixel 7",
    "iPad (gen 6)",
    "Galaxy S9+"
]


@pytest.fixture(scope="session", params=devices)
def mobile_page(request):
    device_name = request.param
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        device = playwright.devices[device_name]
        context = browser.new_context(**device)
        page = context.new_page()
        yield page, device_name
        page.close()
        browser.close()


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as playwright:
        playwright.selectors.set_test_id_attribute("data-test")
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        context.grant_permissions(['geolocation'])
        page = context.new_page()
        yield page
        page.close()
        browser.close()
