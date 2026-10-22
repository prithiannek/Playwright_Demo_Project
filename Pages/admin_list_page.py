class PomAdminListPage:
    def __init__(self, page):
        self.page = page

        self.new_button = page.locator(".btn.btn-rounded.btn-danger").nth(0)  # new button
        self.new_user = page.locator("#username")
        self.password = page.locator("#password")
        self.usertype_field = page.locator("#user_type")
        self.create_button = page.locator("button[name='Create']")

        self.popup_failure = page.locator("//div[contains(@class,'alert-danger')]")
        self.popup_success = page.locator("//div[contains(@class,'alert-success')]")

        self.search_button = page.locator(".btn.btn-rounded.btn-primary")
        self.search_user = page.locator("#un")
        self.search_user_type = page.locator("#ut")
        self.submit_button = page.locator("//button[@type='submit']").nth(0)
        self.result_not_found = page.locator("#res")
        self.result_found = page.locator("//table[contains(@class,'table-bordered')]/tbody/tr[1]/td[1]")

        self.edit_icon = page.locator("//table[contains(@class, 'table-bordered')]/tbody/tr[7]/td[5]/a[2]")
        self.edit_user_type = page.locator("#user_type")
        self.update_button = page.locator("//button[@type='submit']").nth(1)
        self.edit_success_popup = page.locator(".alert.alert-success.alert-dismissible")


    def click_new_button(self):
        self.new_button.click()
        return self

    def enter_new_user(self, new_user):
        self.new_user.fill(new_user)
        return self

    def enter_password(self, password):
        self.password.fill(password)
        return self

    def select_new_usertype(self, staff):
        self.usertype_field.select_option(staff)
        return self

    def click_create_button(self):
        self.create_button.click()
        return self

    # this method is for username already exists case [based on alert-danger]
    def isPopupVisible_failure(self):
        return self.popup_failure.text_content()

    # this method is for user created successfully case [based on alert-success]
    def isPopupVisible_success(self):
        return self.popup_success.text_content()


    def click_search_button(self):
        self.search_button.click()
        return self

    def enter_search_username(self, user):
        self.search_user.fill(user)
        return self

    def select_search_usertype(self, utype):
        self.search_user_type.select_option(utype)
        return self

    def click_submit_button(self):
        self.submit_button.click()
        return self

    def isResultNotFound(self):
        print(self.result_not_found.text_content())

    def isResultFound(self):
        print(f"Result found:{self.result_found.text_content()}")


    def click_edit_icon(self):
        self.edit_icon.click()
        return self

    def enter_new_user_type(self):
        self.edit_user_type.select_option("partner")
        return self

    def click_update_button(self):
        self.update_button.click()
        return self

    def isPopupVisible_EditSuccess(self):
        return self.edit_success_popup.text_content()




