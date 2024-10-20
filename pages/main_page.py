from pages.base_page import BasePage
from pages.locators import MainPageLocators
from playwright.sync_api import expect, Page


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = self.url + "/"

    def navigate_to_about_us(self):
        self.page.locator(MainPageLocators.NAVIGATION_ABOUT_US).click()
        expect(self.page.locator(MainPageLocators.TITLE_ABOUT_US),
               'Секция О нас отображается').to_be_in_viewport()

    def navigate_to_shops(self):
        self.page.locator(MainPageLocators.NAVIGATION_SHOPS).click()
        expect(self.page.locator(MainPageLocators.TITLE_SHOPS),
               'Секция Магазины отображается').to_be_in_viewport()

    def navigate_to_news(self):
        self.page.locator(MainPageLocators.NAVIGATION_NEWS).click()
        expect(self.page.locator(MainPageLocators.TITLE_NEWS),
               'Секция Новости отображается').to_be_in_viewport()

    def navigate_to_faq(self):
        self.page.locator(MainPageLocators.NAVIGATION_HOW).click()
        expect(self.page.locator(MainPageLocators.TITLE_HOW),
               'Секция Как Пользоваться отображается').to_be_in_viewport()

    def navigate_to_map(self):
        self.page.locator(MainPageLocators.NAVIGATION_MAP).click()
        expect(self.page.locator(MainPageLocators.TITLE_MAP),
               'Секция Карта почтоматов отображается').to_be_in_viewport()

    def download_mobile_version_for_android(self):
        with self.page.expect_download() as download_info:
            self.page.locator(MainPageLocators.ANDROID_BUTTON).click()
        download = download_info.value
        filename = download.suggested_filename
        download.delete()
        return filename

    def input_parcel_number(self, parcel_number):
        self.page.get_by_test_id(MainPageLocators.PARCEL_SEARCH_INPUT).press_sequentially(parcel_number, delay=100)
        input_value = self.page.get_by_test_id(MainPageLocators.PARCEL_SEARCH_INPUT).input_value()
        return input_value

    def click_on_search_parcel_button(self):
        self.page.get_by_test_id(MainPageLocators.PARCEL_SEARCH_BUTTON).click()
        expect(self.page, "Нажатие на кнопку найти посылку перенаправляет на страницу B2CPL").to_have_url(
            self.url + "track")
        self.page.go_back()
        expect(self.page, "Успешно вернулись обратно на начальную страницу").to_have_url(
            self.url)

    def open_mobile_version(self, device):
        self.make_screenshot(device)
        expect(self.page.locator(MainPageLocators.PARCEL_SEARCH_BUTTON_MOBILE)).to_be_in_viewport()
        expect(self.page.locator(MainPageLocators.PARCEL_SEARCH_INPUT_MOBILE)).to_be_in_viewport()





