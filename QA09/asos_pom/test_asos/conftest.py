import pytest
from playwright.sync_api import sync_playwright

from QA09.asos_pom.page_asos.brand_page import brandPage
from QA09.asos_pom.page_asos.currency_page import currencyPage
from QA09.asos_pom.test_asos.globals import BASE_URL
from QA09.asos_pom.page_asos.main_page import mainPage




@pytest.fixture()
def setup_asos():
    print("### Test start ###")


    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)

        main_page = mainPage(page)
        currency_page = currencyPage(page)
        brand_page = brandPage(page)



        yield page,main_page, currency_page, brand_page
        print("### Test end ###")
        page.close()
        browser.close()