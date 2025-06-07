from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    REMOVE_SELECTOR = ".cart_item >> text='Remove'"
    RETURN_SELECTOR = ".cart_footer >> text='Continue Shopping'"
    CHECKOUT_SELECTOR = "#checkout"


    def remove_item_from_cart(self):
        self.wait_for_selector_click(self.REMOVE_SELECTOR)
        #self.assert_element_is_not_visible(self.REMOVE_SELECTOR)

    def continue_shopping(self):
        self.wait_for_selector_click(self.RETURN_SELECTOR)
        self.assert_text_present_on_page('Products')

    def go_to_checkout_cart(self):
        self.wait_for_selector_click(self.CHECKOUT_SELECTOR)
        self.assert_text_present_on_page('Checkout: Your Information')