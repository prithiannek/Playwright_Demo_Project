class POMCheckoutPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")

    def enter_first_name(self, first_name):
        self.first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name.fill(last_name)

    def enter_zip_code(self, zip_code):
        self.zip_code.fill(zip_code)

    def click_continue_button(self):
        self.continue_button.click()