


class mainPage:
    def __init__(self, page):
        self.page = page

    def verify_titles(self, text):
        search_bar = self.page.locator("[id= 'chrome-search']")                       # insert wanted request in search bar
        search_bar.fill(text)
        search_button = self.page.get_by_role("img", name="search")
        search_button.click()
        titles = self.page.query_selector_all("[class='productDescription_sryaw']")   # uploading all items by that title
        titles = titles[:5]                                                           # returning only the first 5 results
        if not titles:                                                                # if: no results = assertion
            raise AssertionError(f" no title were found '{text}'")
        text = text.lower()                                                           # returning result as singular or plurals
        singular = text.rstrip('s')
        plural = singular + 's'
        for title in titles:
            title_text = title.text_content()
            print(title_text)
            if singular not in title_text and plural not in title_text:               # if: result incorrect = get assertion
                raise AssertionError(f" the word '{text}' wasn't found in {title_text}")
