     # A test to verify currency updates the prices to selected currency

class currencyPage:
    def __init__(self, page):
        self.page = page

    def currency_change(self):
        women_button = self.page.locator("[id= 'women-floor']")                              # click "woman" button
        women_button.click()
        new_in_checkbox = self.page.get_by_role("button", name="New in")                     # click "new in" button
        new_in_checkbox.click()
        summer_essentials_link = self.page.get_by_role("link", name="Summer Essentials")     # click "summer essentials" link
        summer_essentials_link.click()
        israel_button = self.page.locator("[class= 'RxHz4Yh']")                              # click the flag button in the right corner
        israel_button.click()
        ils_select = self.page.locator("[id= 'currency']")
        ils_select.click()
        self.page.select_option("#currency", value="2")                                      # click on the USD currency
        update_preferences_button = self.page.get_by_text("UPDATE PREFERENCES")              # click UPDATE PREFERENCES to confirm
        update_preferences_button.click()
        ils_currency = self.page.content()
        count_ils = ils_currency.count("ILS")                                               # confirm that all the prices changed to USD
        print(f"'ILS' appears {count_ils} times in this page")                              # and no ILS remained
        assert count_ils == 0, "'ILS' is not appeared in this page"
