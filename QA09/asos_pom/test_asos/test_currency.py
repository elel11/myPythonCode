

class TestCurrency:

    def test_currency(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page = setup_asos
        currency_page.currency_change()

        # this test detected a bug - Despite selecting USD via code and
        # confirming that the correct option is visually marked as selected,
        # the preference reverts back to ILS (₪).

        # ils_select = self.page.locator("[id= 'currency']")
        # ils_select.click()
        # self.page.select_option("#currency", value="2")
        # update_preferences_button = self.page.get_by_text("UPDATE PREFERENCES")
        # update_preferences_button.click()
