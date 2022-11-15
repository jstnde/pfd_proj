from page_objects.login_page import LoginPage


class LoginTest(LoginPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.open_page()

    # Test Case 1 : Successful Login
    def test_login(self):
        self.type(LoginPage.input_field_username, LoginPage.input_value_username)
        self.type(LoginPage.input_field_password, LoginPage.input_value_password)

        print("Input right testing username : '" + LoginPage.input_value_username + "'")
        print("Input right testing password : '" + LoginPage.input_value_password + "'")

        self.scroll_to(LoginPage.input_field_password)
        self.save_screenshot("form_field",
                             LoginPage.custom_screenshot_dir +
                             "/test_login")

        self.click(LoginPage.submit_btn)

        print("Click Submit button")

        self.save_screenshot("products_page",
                             LoginPage.custom_screenshot_dir +
                             "/test_login")

        self.assert_text("Index", "h1")

        print("Successful sign in")

    # Test Case 2 : Unsuccessful Login
    def test_login_error_msg(self):
        self.type(LoginPage.input_field_username, LoginPage.input_value_invalid_username)
        self.type(LoginPage.input_field_password, LoginPage.input_value_password)

        print("Input wrong testing username : '" + LoginPage.input_value_invalid_username + "'")
        print("Input right testing password : '" + LoginPage.input_value_password + "'")

        self.scroll_to(LoginPage.input_field_password)
        self.save_screenshot("form_field",
                             LoginPage.custom_screenshot_dir +
                             "/test_login_error_msg")

        self.click(LoginPage.submit_btn)

        print("Click Submit button")

        self.scroll_to(LoginPage.error_span)
        self.save_screenshot("error_msg",
                             LoginPage.custom_screenshot_dir +
                             "/test_login_error_msg")

        self.assert_true(self.is_text_visible(LoginPage.error_text, LoginPage.error_span))

        print("Error message '" + LoginPage.error_text + "' appears")
