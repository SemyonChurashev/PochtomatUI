from pages.main_page import MainPage
from pages.assertions import Assertions
import pytest


@pytest.mark.pcbrowser
def test_navigation_to_section(page):
    main_page = MainPage(page)
    main_page.open_page()
    main_page.navigate_to_about_us()
    main_page.navigate_to_news()
    main_page.navigate_to_shops()
    main_page.navigate_to_map()
    main_page.navigate_to_faq()


@pytest.mark.pcbrowser
def test_parcel_search_input(page):
    main_page = MainPage(page)
    main_page.open_page()
    parcel_number = "PQ-AX-12323-FDHSJD-РУ"
    entered_value = main_page.input_parcel_number(parcel_number)
    Assertions.check_entered_value(entered_value, parcel_number)


@pytest.mark.pcbrowser
def test_mobile_version_download(page):
    main_page = MainPage(page)
    main_page.open_page()
    file = main_page.download_mobile_version_for_android()
    Assertions.check_apk_file_version(file)


@pytest.mark.pcbrowser
def test_parcel_search_button_redirection(page):
    main_page = MainPage(page)
    main_page.open_page()
    main_page.click_on_search_parcel_button()


@pytest.mark.mobilebrowser
def test_mobile_versions(mobile_page):
    mobile_page, device_name = mobile_page
    main_page = MainPage(mobile_page)
    main_page.open_page()
    main_page.open_mobile_version(device_name)
