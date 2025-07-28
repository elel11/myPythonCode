from QA09.swaglabs_pom.tests.conftest import setup_swaglabs


class TestProduct():


    def test_verify_prices_less_than_100(self, setup_swaglabs):
        page, login_page, product_page =  setup_swaglabs
        login_page.login("standard_user", "secret_sauce")
        product_page.verify_product_prices()

    # def test_login_by_css(self, setup_swaglabs):
    #     page = setup_swaglabs
    #     page.goto("https://www.ebay.com/")
    #     user = page.locator("input[id= 'user-name']")
    #     password = page.locator("input[data-test= 'password']")
    #     login_button = page.locator("input[class= 'submit-button btn_action']")
    #     user.fill("abc")
    #     password.fill("fake")
    #     login_button.click()
    #     print("debug point")