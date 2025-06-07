from playwright.sync_api import sync_playwright
import time

def test_order():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")

    # логинимся
    page.is_visible(selector='[id="user-name"]')
    page.type(selector='[id="user-name"]', text='standard_user', delay=100)
    page.type(selector='[id="password"]', text='secret_sauce', delay=100)
    page.click('.submit-button') # [class='submit-button']

    # добавляем в корзину
    page.is_enabled(selector='[id="add-to-cart-sauce-labs-backpack"]')
    page.click(selector='[id="add-to-cart-sauce-labs-backpack"]')

    # заходим в корзину
    page.is_enabled(selector='[data-test="shopping-cart-link"]')
    page.click(selector='[data-test="shopping-cart-link"]')

    # удаляем товар из корзины
    #page.is_enabled(selector='[id="remove-sauce-labs-backpack"]')
    #page.click(selector='[id="remove-sauce-labs-backpack"]')

    # переход к заполнению данных покупателя
    page.is_enabled(selector='[id="checkout"]')
    page.click(selector='[id="checkout"]')

    # вводим данные покупателя
    page.wait_for_selector(selector='[id="first-name"]', state='attached')
    page.type(selector='[id="first-name"]', text='Говночист', delay=60)
    page.type(selector='[id="last-name"]', text='Не шофёр', delay=60)
    page.type(selector='[id="postal-code"]', text='12345', delay=60)

    # подтверждаем данные
    page.wait_for_selector(selector='[id="continue"]', state='attached')
    page.click(selector='[id="continue"]')

    # оформляем заказ
    page.wait_for_selector(selector='[id="finish"]', state='attached')
    page.click(selector='[id="finish"]')

    assert page.is_visible(selector='[data-test="complete-header"]') == True, 'Заказ не оформлен'

    # заходим в бургер-меню
    page.wait_for_selector(selector='[id="react-burger-menu-btn"]', state='attached')
    page.click(selector='[id="react-burger-menu-btn"]')

    # выходим из аккаунта
    page.wait_for_selector(selector='[id="logout_sidebar_link"]', state='attached')
    page.click(selector='[id="logout_sidebar_link"]')

    time.sleep(3)

    browser.close()

    playwright.stop()