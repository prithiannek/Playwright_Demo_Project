class PomSauceDemoItemDescriptionPage:
    def __init__(self, page):
        self.page = page
        self.item_name = page.locator(".inventory_details_name.large_size")
        self.add_to_cart = page.locator("#add-to-cart")
        self.back_to_products_link = page.locator("#back-to-products")
        self.go_to_cart_link = page.locator(".shopping_cart_link")
        self.menu = page.locator("#react-burger-menu-btn")

    def check_item_name(self):
        return self.item_name.text_content()

    def add_product_to_cart(self):
        self.add_to_cart.click()

    def navigate_back_to_dashboard(self):
        self.back_to_products_link.click()
        