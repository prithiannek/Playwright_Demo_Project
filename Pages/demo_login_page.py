class PomDemoLoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.locator("button[type='submit']")


    def enter_username(self, username):
        self.username.fill(username)
        return self

    def enter_password(self, password):
        self.password.fill(password)
        return  self

    def click_login(self):
        from Pages.demo_admin_page import PomDemoAdminPage
        self.login_button.click()
        return PomDemoAdminPage(self.page)
    # This process is called circular import.
    # In case of testcases chaining method can be implemented between methods
    # as well as POM pages.

    