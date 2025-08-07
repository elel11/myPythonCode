class brandPage:
    def __init__(self, page):
        self.page = page

    def brand_test(self):
        women_button = self.page.locator("[id= 'women-floor']")                         # click on "woman" button
        women_button.click()
        sale_button = self.page.get_by_role("button", name="Sale")                      # click on "sale" button
        sale_button.click()
        size_12_button = self.page.get_by_text("Size 12")                              # click on "size 12" button
        size_12_button.click()
        brand_button = self.page.get_by_role("button", name="Brand")                   # click on "brand" button
        brand_button.click()
        asos_maternity_link = self.page.get_by_text("ASOS Maternity")                  # click on "ASOS MATERNITY" button
        asos_maternity_link.click()
        asos_maternity_description = self.page.query_selector_all("[class= 'productDescription_sryaw']")      # upload all the item by
        descriptions = asos_maternity_description                                                             # the same title
        all_match = True
        for description in descriptions:
            text = description.text_content()
            print(text)
            if "ASOS DESIGN Maternity" not in text:                                     # if: the title not in one of the
                all_match = False                                                       # titles = get assertion

        if all_match:
            assert True
        else:
            print("test failed")
            assert False

