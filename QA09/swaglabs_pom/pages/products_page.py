

class productPage():
    def __init__(self,page):
        self.page = page

    def verify_product_prices(self):
        prices = self.page.query_selector_all("[class='inventory_item_price']")

        for price in prices:
            price_as_str = price.text_content()
            print(price_as_str)
            price_as_str = price_as_str.replace("$", "")
            price_as_float = float(price_as_str)
            is_pass = price_as_float < 100  # getting results as boolean
            assert is_pass, "the Price is more than 100$"
        print("after query selector all")



def test_login_by_css(self, setup_swaglabs):
    page = setup_swaglabs
    page.goto("https://www.ebay.com/")
    user = page.locator("input[id= 'user-name']")
    password = page.locator("input[data-test= 'password']")
    login_button = page.locator("input[class= 'submit-button btn_action']")
    user.fill("abc")
    password.fill("fake")
    login_button.click()
    print("debug point")
