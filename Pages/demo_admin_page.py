class PomDemoAdminPage:
    def __init__(self, page):
        self.page = page
        self.more_info = page.locator(".small-box-footer").nth(1)
        self.admin_icon = page.locator("a[data-toggle='dropdown']")
        self.logout_option = page.locator("a[class='dropdown-item']").nth(1)
        self.all_more_info_links = page.locator(".small-box-footer")

    def click_more_info_link(self):
        from Pages.admin_list_page import PomAdminListPage
        self.more_info.click()
        return PomAdminListPage(self.page)

    def click_admin_icon(self):
        self.admin_icon.click()
        return self

    def click_logout_option(self):
        from Pages.demo_login_page import PomDemoLoginPage
        self.logout_option.click()
        return PomDemoLoginPage(self.page)


    def count_more_info_link(self):
        return self.all_more_info_links.count()
