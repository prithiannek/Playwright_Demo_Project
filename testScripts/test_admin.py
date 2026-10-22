from playwright.sync_api import Page, expect
from constants.constant import login_url
from Pages.admin_list_page import PomAdminListPage
from Pages.demo_admin_page import PomDemoAdminPage
from Pages.demo_login_page import PomDemoLoginPage

import pytest
class TestAdminRights:
    #@pytest.mark.flaky(rerun=3)
    def test_admin_add_user(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("button[type='submit']").click()
        page.locator(".small-box-footer").nth(1).click() #more info link
        page.locator(".btn.btn-rounded.btn-danger").nth(0).click() #new button
        page.locator("#username").fill("PrithiA")
        page.locator("#password").fill("Prithi@123")
        page.select_option("#user_type", label = 'Staff')
        page.locator(".card.card-dark").nth(1).screenshot(path="screenshots/image3.png")
        page.locator("button[name='Create']").click()
        alert = page.locator(".alert.alert-success.alert-dismissible")
        expect(alert).to_be_visible()

    def test_admin_add_existing_user(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("button[type='submit']").click()
        page.locator(".small-box-footer").nth(1).click() #more info link
        page.locator(".btn.btn-rounded.btn-danger").nth(0).click() #new button
        page.locator("#username").fill("PrithiA")
        page.locator("#password").fill("Prithi@123")
        page.select_option("#user_type", label = 'Staff')
        page.locator("button[name='Create']").click()
        alert = page.locator(".alert.alert-danger.alert-dismissible")
        expect(alert).to_contain_text("Username already exists.")


    def test_admin_listpage_pom(self, page:Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        admin = PomDemoAdminPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        admin.click_more_info_link()

        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/list-admin")
        print("Successfully navigated to Admin List Page!")


    def test_admin_add_user_pom(self, page: Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)
        new = PomAdminListPage(page)


        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.click_more_info_link()

        new.click_new_button()
        new.enter_new_user("Prithi Annn Kurien")
        new.enter_password("prithi1234")
        new.select_new_usertype("staff")
        new.click_create_button()

        new.isPopupVisible_success()


    def test_admin_add_existing_user_pom(self, page: Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)
        new = PomAdminListPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.click_more_info_link()

        new.click_new_button()
        new.enter_new_user("Prithi Anne Kurien")
        new.enter_password("prithi123")
        new.select_new_usertype("staff")
        new.click_create_button()

        new.isPopupVisible_failure()


    def test_admin_search_valid_user_pom(self, page: Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)
        search = PomAdminListPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.click_more_info_link()

        search.click_search_button()
        search.enter_search_username("Liju")
        search.select_search_usertype("staff")
        search.click_submit_button()
        expect(search.result_found).to_have_text(search.search_user.input_value())
        print(f"User {search.isResultFound()} found!")


    def test_admin_search_invalid_user_pom(self, page: Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)
        search = PomAdminListPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.click_more_info_link()

        search.click_search_button()
        search.enter_search_username("Liju")
        search.select_search_usertype("admin")
        search.click_submit_button()
        expect(search.result_not_found).to_contain_text(".........RESULT NOT FOUND.......")
        print("User not found!")


    def test_admin_dashboard_slide_count_pom(self, page: Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.count_more_info_link()
        expect(dashboard.all_more_info_links).to_have_count(10)
        print(f"The are {dashboard.count_more_info_link()} slides")


    def test_admin_edit_user_pom(self, page:Page):
        page.goto(login_url)

        login = PomDemoLoginPage(page)
        dashboard = PomDemoAdminPage(page)
        edit = PomAdminListPage(page)

        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        dashboard.click_more_info_link()

        edit.click_edit_icon()
        edit.select_new_usertype("partner")
        edit.click_update_button()
        #edit.isPopupVisible_EditSuccess()
        expect(edit.edit_success_popup).to_be_visible()
        print("User updated successfully")

#POM chaining for admin user addition
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_admin_add_user_with_pomchaining(self, page: Page):
        page.goto(login_url)
        login = PomDemoLoginPage(page)
        login.enter_username("admin").enter_password("admin").click_login().click_more_info_link().click_new_button().enter_new_user("Prithi Anne").enter_password("jose123").select_new_usertype("staff").click_create_button()
        expect(page.locator("//div[contains(@class,'alert-success')]")).to_be_visible()
        print("User added successfully!")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_admin_add_existing_user_with_pomchaining(self, page: Page):
        page.goto(login_url)
        login = PomDemoLoginPage(page)
        login.enter_username("admin").enter_password("admin").click_login().click_more_info_link().click_new_button().enter_new_user("Lizbeth").enter_password("lizbeth123").select_new_usertype("staff").click_create_button()
        expect(page.locator("//div[contains(@class,'alert-danger')]")).to_be_visible()
        print("User already exists!")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.endtoend
    def test_admin_search_valid_user_with_pomchaining(self, page: Page):
        page.goto(login_url)
        login = PomDemoLoginPage(page)
        login.enter_username("admin").enter_password("admin").click_login().click_more_info_link().click_search_button().enter_search_username("Liju").select_search_usertype("staff").click_submit_button().isResultFound()


#Difference between debugging tools, screenshots, video and trace
#Screenshot: Captures the webpage at a particular moment.  Useful for checking error messages
#and incorrect ui elements.

#Video Recording: Records the browser while the test runs. Useful for viewing the sequence of
#actions leading to a success or failure.

#Trace viewer: Records actions, network activity, dom snapshots, console information and timing details.
#Most informative option when debugging a failed testcase.

#Screenshot:
#Case1: Capture the current visible page. Captures the current viewport.
#page.screenshot(path="file.png")

#Case2: Capture the full web page. Captures the entire scrollable page.
#page.screenshot(path="file.png", full_page=True)

#Case3: Capture an element only. (Heading, button, form, table, etc.)
#page.locator("#h1").screenshot(path="file.png")
#page.get_by_text("Welcome").screenshot(path="file.png")

#Commands:
#1. pytest --screenshot=only-on-failure
#2. pytest --screenshot=on
#3. pytest --screenshot=off











