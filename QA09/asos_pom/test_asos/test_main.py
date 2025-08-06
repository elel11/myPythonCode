from QA09.asos_pom.page_asos.globals import SEARCH_ON_SEARCH_BAR, SEARCH_ON_SEARCH_BAR_2, FAKE_SEARCH_ON_SEARCH_BAR


class TestMain():


    def test_verify_titles_shoes(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page = setup_asos
        main_page.verify_titles(SEARCH_ON_SEARCH_BAR)

    def test_verify_titles_shirt(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page = setup_asos
        main_page.verify_titles(SEARCH_ON_SEARCH_BAR_2)

    def test_verify_titles_fake(self, setup_asos):
        page, main_page, high_low_page, currency_page, brand_page = setup_asos
        main_page.verify_titles(FAKE_SEARCH_ON_SEARCH_BAR)
