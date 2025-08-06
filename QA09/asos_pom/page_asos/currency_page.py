class currencyPage:
    def __init__(self, page):
        self.page = page

    def currency_change(self):
        women_button = self.page.locator("[id= 'women-floor']")
        women_button.click()
        new_in_checkbox = self.page.get_by_role("button", name="New in")
        new_in_checkbox.click()
        summer_essentials_link = self.page.get_by_role("link", name="Summer Essentials")
        summer_essentials_link.click()
        israel_button = self.page.locator("[class= 'RxHz4Yh']")
        israel_button.click()
        ils_select = self.page.locator("[id= 'currency']")
        ils_select.click()
        self.page.select_option("#currency", value="2")
        update_preferences_button = self.page.get_by_text("UPDATE PREFERENCES")
        update_preferences_button.click()
        ils_currency = self.page.content()
        count_ils = ils_currency.count("ILS")
        print(f"'ILS' appears {count_ils} times in this page")
        assert count_ils == 0, "'ILS' is not appeared in this page"
