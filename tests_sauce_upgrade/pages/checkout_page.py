from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    FIRSTNAME_SELECTOR = '#first-name'
    LASTNAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = '#postal-code'
    CONTINUE_SELECTOR = '#continue'
    CANCEL_SELECTOR = '#cancel'

    def first_checkout_step(self, data):
        self.wait_for_selector_fill(self.FIRSTNAME_SELECTOR, data[0])
        self.wait_for_selector_fill(self.LASTNAME_SELECTOR, data[1])
        self.wait_for_selector_fill(self.POSTAL_CODE_SELECTOR, data[2])
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, data[2])

        self.wait_for_selector_click(self.CONTINUE_SELECTOR)
        self.assert_text_present_on_page('Checkout: Overview')