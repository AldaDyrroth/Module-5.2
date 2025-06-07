from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage

def test_add_items(browser, userdata):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.authorization('standard_user', 'secret_sauce')

    inventory_page.add_item_to_cart()
    inventory_page.remove_item_from_cart()
    #inventory_page.sort_items_by_price_growing()
    #inventory_page.sort_items_by_title_z_to_a()
    inventory_page.add_item_to_cart()
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart_page()

    cart_page.remove_item_from_cart()
    cart_page.go_to_checkout_cart()
    # cart_page.continue_shopping()

    checkout_page.first_checkout_step(userdata)

