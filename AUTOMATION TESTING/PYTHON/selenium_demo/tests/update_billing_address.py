import random
import pytest

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0, 10000)) + "jankowalski@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'jankowalsk')
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Doe")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Kwiatowa 1", "00-001", "Pcim Dolny")
        billing_address_page.set_phone_number("000-000-000")
        billing_address_page.save_address()

        assert 'Address changed successfully.' in billing_address_page.get_message_text()
