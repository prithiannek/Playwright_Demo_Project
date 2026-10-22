class POMOrderPlacedPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.order_confirmation_heading = page.locator(".complete-header")
        self.back_home = page.locator("#back-to-products")
        self.generate_pdf = page.locator("#generate-pdf-order")
        self.menu = page.locator("#react-burger-menu-btn")
        self.cart_icon = page.locator(".shopping_cart_link")

    def check_order_confirmation(self):
        return self.order_confirmation_heading.text_content()

    def click_generate_pdf(self):
        self.generate_pdf.click()