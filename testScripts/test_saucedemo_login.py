from playwright.sync_api import Page, expect
from Pages.saucedemo_login_page import POMLoginPage
from Pages.saucedemo_cart_page import POMCartPage
from Pages.saucedemo_payment_page import POMPaymentPage
from Pages.saucedemo_checkout_page import POMCheckoutPage
from Pages.saucedemo_dashboard_page import PomSauceDemoDashboardPage
from Pages.saucedemo_order_placed_page import POMOrderPlacedPage
from Pages.saucedemo_item_description_page import PomSauceDemoItemDescriptionPage
from constants.constant import login_url2
import pytest

class TestSauceDemoLogin:
    @pytest.mark.timeout(100)
    def test_valid_login(self, page:Page):
        page.goto(login_url2)
        login = POMLoginPage(page)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("Successfully logged in!")
