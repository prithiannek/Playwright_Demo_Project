class PomSauceDemoDashboardPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.menu = page.locator("#react-burger-menu-btn")
        self.sort_icon = page.locator(".product_sort_container")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.item_slide = page.locator(".inventory_item").nth(0)
        self.add_to_cart_button = page.get_by_text("Add to cart").nth(0)


    def check_title(self):
        return self.title.text_content()

    def click_item(self):
        self.item_slide.click()

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_go_to_cart(self):
        self.cart_icon.click()