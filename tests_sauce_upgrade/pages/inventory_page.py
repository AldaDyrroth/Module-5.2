from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    GOOD_SELECTOR = ".inventory_item >> text='Add to cart'"
    GOOD_2_SELECTOR = ".inventory_item >> text='Sauce Labs Bolt T-Shirt'"
    RED_MARK_SELECTOR = '.shopping_cart_badge'
    REMOVE_SELECTOR = ".inventory_item >> text='Remove'"
    SORTING_SELECTOR = ".product_sort_container"
    SORT_PARAM_PRICE_SELECTOR = ".product_sort_container >> text='Price (low to high)'"
    SORT_PARAM_NAME_SELECTOR = ".product_sort_container >> text='Price (low to high)'"


    def add_item_to_cart(self):
        self.wait_for_selector_click(self.GOOD_SELECTOR)
        self.assert_element_is_visible(self.RED_MARK_SELECTOR)


    def remove_item_from_cart(self):
        self.wait_for_selector_click(self.REMOVE_SELECTOR)
        self.assert_element_is_not_visible(self.RED_MARK_SELECTOR)


    def sort_items_by_price_growing(self, min_price='7.99', max_price='49.99'):
        self.wait_for_selector_click(self.SORTING_SELECTOR)
        self.wait_for_selector_click(self.SORT_PARAM_PRICE_SELECTOR)
        self.assert_text_in_first_element(self.GOOD_SELECTOR, min_price)
        self.assert_text_in_last_element(self.GOOD_SELECTOR, max_price)

        self.wait_for_selector_click(self.RED_MARK_SELECTOR)
        self.assert_text_present_on_page('Your Cart')

    def sort_items_by_title_z_to_a(self,
                                   first_title='Test.allTheThings() T-Shirt (Red)',
                                   last_title='Sauce Labs Backpack'):
        self.wait_for_selector_click(self.SORTING_SELECTOR)
        self.wait_for_selector_click(self.SORT_PARAM_SELECTOR)
        self.assert_text_in_first_element(self.GOOD_SELECTOR, first_title)
        self.assert_text_in_last_element(self.GOOD_SELECTOR, last_title)

    def go_to_cart_page(self):
        self.wait_for_selector_click(self.RED_MARK_SELECTOR)
        self.assert_text_present_on_page('Your Cart')