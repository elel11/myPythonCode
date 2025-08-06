class mainPage:
    def __init__(self, page):
        self.page = page

    def verify_titles(self, text):
        search_bar = self.page.locator("[id= 'chrome-search']")
        search_bar.fill(text)
        search_button = self.page.get_by_role("img", name="search")
        search_button.click()
        self.page.wait_for_timeout(3000)
        titles = self.page.query_selector_all("[class='productDescription_sryaw']")
        titles = titles[:5]
        if not titles:
            raise AssertionError(f" no title were found '{text}'")
        text = text.lower()
        singular = text.rstrip('s')
        plural = singular + 's'
        for title in titles:
            title_text = title.text_content()
            print(title_text)
            if singular not in title_text and plural not in title_text:
                raise AssertionError(f" the word '{text}' wasn't found in {title_text}")
