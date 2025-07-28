import time


class TestLogin():



    def test_login_Correct_parameters(self, setup_swaglabs):

        page , login_page , product_page = setup_swaglabs
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)
        login_page.verify_login_success()


    def test_login_Incorrect_user(self, setup_swaglabs):

        page , login_page , product_page = setup_swaglabs
        login_page.login("fake_user", "secret_sauce")
        time.sleep(3)
        login_page.verify_login_fail()


    def test_login_Incorrect_password(self, setup_swaglabs):

        page , login_page , product_page = setup_swaglabs
        login_page.login("standard_user", "fake_password")
        time.sleep(3)
        login_page.verify_login_fail()




