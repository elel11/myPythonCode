# A test to verify currency updates the prices to selected currency

class TestCurrency:

    def test_currency(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page = setup_asos
        currency_page.currency_change()

        # this test detected a bug - Despite selecting USD via code and
        # confirming that the correct option is visually marked as selected,
        # the preference reverts back to ILS (₪).


