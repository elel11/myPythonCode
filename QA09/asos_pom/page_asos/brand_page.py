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
        self.page.wait_for_selector(".productDescription_sryaw")                       #  waiting for titles to upload
        asos_maternity_description = self.page.locator("[class= productDescription_sryaw]")    # uploading all items by that title
        count = asos_maternity_description.count()
        print("found", count, "items")                                                 # print all items found
        descriptions = asos_maternity_description
        expected = "asos design maternity"
        all_match = True
        for i in range(count):                                                         # getting all the titles and inspect them
            description = asos_maternity_description.nth(i)
            text = description.text_content().lower()
            print(text)
            if expected not in text:
                all_match = False
            if expected not in text:                                                    # if: the title not in one of the
                all_match = False                                                       # titles = get assertion

        if all_match:
            assert True
        else:
            print("test failed")
            assert False

