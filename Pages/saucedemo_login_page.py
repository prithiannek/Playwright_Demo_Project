class POMLoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def enter_username(self, username):
        self.username_field.fill(username)

    def enter_password(self, password):
        self.password_field.fill(password)

    def click_login(self):
        self.login_button.click()

