class POMPaymentPage:
    def __init__(self, page):
        self.page = page
        self.payment_title = page.locator(".title")
        self.finish_button = page.locator("#finish")
        self.cancel = page.locator("#cancel")
        self.menu = page.locator("#react-burger-menu-btn")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_item = page.locator(".cart_item").nth(0)

    def check_title(self):
        return self.payment_title.text_content()

    def check_cart_item(self):
        return self.cart_item.count()

    def click_finish_button(self):
        self.finish_button.click()