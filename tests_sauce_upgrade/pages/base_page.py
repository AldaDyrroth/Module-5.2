from playwright.sync_api import expect

class BasePage:
    __BASE_URL = 'https://www.saucedemo.com'


    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self):
        return f'{self.__BASE_URL}/{self._endpoint}'

    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_fill(self, selector, text):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    def wait_for_selector_type(self, selector, text, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, text, delay=delay)

    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def assert_element_is_not_visible(self, selector):
        expect(self.page.locator(selector)).not_to_be_visible()

    def assert_text_present_on_page(self, title):
        expect(self.page.locator("body")).to_contain_text(title)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_text_in_first_element(self, selector, text):
        expect(self.page.locator(selector).first).to_have_text(text)

    def assert_text_in_last_element(self, selector, text):
        expect(self.page.locator(selector).last).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)

