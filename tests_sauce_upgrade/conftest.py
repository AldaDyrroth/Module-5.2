from playwright.sync_api import sync_playwright
import time
from faker import Faker
faker = Faker()
import pytest

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    time.sleep(3)

    browser.close()

    playwright.stop()

@pytest.fixture(scope="session")
def userdata():
    return [
        faker.first_name(),
        faker.last_name(),
        faker.postcode()
    ]
