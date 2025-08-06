class brandPage:
    def __init__(self, page):
        self.page = page

    def brand_test(self):
        women_button = self.page.locator("[id= 'women-floor']")
        women_button.click()
        sale_button = self.page.get_by_role("button", name="Sale")
        sale_button.click()
        size_12_button = self.page.get_by_text("Size 12")
        size_12_button.click()
        brand_button = self.page.get_by_role("button", name="Brand")
        brand_button.click()
        asos_maternity_link = self.page.get_by_text("ASOS Maternity")
        asos_maternity_link.click()
        asos_maternity_description = self.page.query_selector_all("[class= 'productDescription_sryaw']")
        descriptions = asos_maternity_description
        all_match = True
        for description in descriptions:
            text = description.text_content()
            print(text)
            if "ASOS DESIGN Maternity" not in text:
                all_match = False

        if all_match:
            assert True
        else:
            print("test failed")
            assert False

