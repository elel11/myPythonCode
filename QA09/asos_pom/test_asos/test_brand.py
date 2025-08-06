


class TestBrand:

    def test_brand(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page  = setup_asos
        brand_page.brand_test()