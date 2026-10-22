class POMCartPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.remove_button = page.get_by_text("Remove").nth(0)
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.cart_item = page.locator(".cart_item")
        self.go_to_cart_link = page.locator(".shopping_cart_link")
        self.menu = page.locator("#react-burger-menu-btn")

    def check_title(self):
        return self.title.text_content()

    def check_cart_item(self):
        return self.cart_item.count()

    def click_checkout_button(self):
        self.checkout_button.click()
