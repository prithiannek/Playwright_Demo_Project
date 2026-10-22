from playwright.sync_api import Page, expect


from constants.constant import login_url
from utilities.excel_read import NewExcelReader
from Pages.saucedemo_login_page import POMLoginPage
from Pages.demo_login_page import PomDemoLoginPage
from Pages.demo_admin_page import PomDemoAdminPage
import pytest
class TestLogin:
    def test_valid_login(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("adminn")
        #page.get_by_text("Sign In").click() -----resolved to 2 elements
        page.locator("button[type='submit']").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    def test_valid_login_excel(self, page:Page):
        page.goto(login_url)
        obj = NewExcelReader()
        username = obj.read_excel_cell(2,1)
        password = obj.read_excel_cell(2,2)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.locator("button[type='submit']").click()
        expect(page).to_have_title("Dashboard | 7rmart supermarket")


    def test_invalid_login(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("1234")
        page.locator("button[type='submit']").click()
        alert_class = page.locator(".alert.alert-danger.alert-dismissible")
        expect(alert_class).to_contain_text("Invalid Username/Password")

    def test_invalid_login_excel(self, page:Page):
        page.goto(login_url)
        obj = NewExcelReader()
        username = obj.read_excel_cell(3,1)
        password = obj.read_excel_cell(3,2)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.locator("button[type='submit']").click()
        alert_class = page.locator(".alert.alert-danger.alert-dismissible")
        expect(alert_class).to_be_visible()

    def test_admin_dashboard(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("button[type='submit']").click()
        slides = page.locator(".col-lg-3.col-6")
        count = slides.count()
        expect(slides).to_have_count(count)

    def test_admin_logout(self, page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("button[type='submit']").click()
        page.locator("a[data-toggle='dropdown']").click() #admin icon
        page.locator("a[class='dropdown-item']").nth(1).click() #logout option
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")

#
#
#
#Test cases using POM
#New site: https://www.saucedemo.com/
    @pytest.mark.order(2)
    def test_saucedemo_login_pom(self, page:Page):
        page.goto("https://www.saucedemo.com/")
        log = POMLoginPage(page) #object creation and fixture passing. Constructor gets called while creating object.
        log.enter_username("standard_user")
        log.enter_password("secret_sauce")
        log.click_login()

#using demo project: https://groceryapp.uniqassosiates.com/admin/login
    @pytest.mark.order(1)
    def test_valid_login_pom(self, page:Page):
        page.goto(login_url)
        demo = PomDemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin123")
        page.screenshot(path="screenshots/image1.png")
        demo.click_login()
        page.screenshot(path="screenshots/image2.png")
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
        print("Successfully logged in!")




    def test_admin_logout_pom(self, page:Page):
        page.goto(login_url)

        demo = PomDemoLoginPage(page)
        admin = PomDemoAdminPage(page)

        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_login()
        admin.click_admin_icon()
        admin.click_logout_option()

        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")
        print("Successfully logged out!")

#POM chaining using login pom alone
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_admin_login_with_pomchaining(self, page:Page):
        page.goto(login_url)
        demo = PomDemoLoginPage(page)
        demo.enter_username("admin").enter_password("admin").click_login()

#Using pom chaining for logout - connecting login pom and admin dashboard pom
    def test_valid_admin_logout_with_pomchaining(self, page:Page):
        page.goto(login_url)
        demo = PomDemoLoginPage(page)
        demo.enter_username("admin").enter_password("admin").click_login().click_admin_icon().click_logout_option()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")
        print("Successfully logged out!")



    def test_valid_login_pom2(self, page:Page):
        page.goto(login_url)
        demo = PomDemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        page.screenshot(path="screenshots/image1.png", full_page=True)
        demo.click_login()
        page.screenshot(path="screenshots/image2.png", full_page=True)
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
        print("Successfully logged in!")

"""Allure Report is an open-source framework-agnostic test result visualization tool.
ü  it is developed by Qameta Software along with open-source community contributors
ü  It transforms test execution data into clear, interactive HTML reports.
ü  It works with popular testing frameworks across JavaScript, Python, Java, C#, PHP, and Ruby, helping teams track test results and better manage software quality.
"""
