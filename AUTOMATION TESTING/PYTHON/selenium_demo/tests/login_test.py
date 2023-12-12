from pages.my_account_page import MyAccountPage
import pytest


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("jankowalski@gmail.com", "jankowalsk")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("jankowalski@gmail.com", "jankowalski123")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
    
