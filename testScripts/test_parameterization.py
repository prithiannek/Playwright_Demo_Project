from playwright.sync_api import Page, expect


class TestParameterization:
    import pytest
    @pytest.mark.parametrize("valid_usernames", ["standard_user", "locked_out_user", "problem_user"])
    def test_valid_login_parameterization(self, page:Page, valid_usernames):
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill(valid_usernames)
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("Login successful!")