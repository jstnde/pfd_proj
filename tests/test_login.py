from page_objects.login_page import LoginPage


class LoginTest(LoginPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.open_page()

    # Test Case 1 : Login
    def test_login(self):
        self.send_keys(LoginPage.input_field_username, LoginPage.input_value_username)
        self.send_keys(LoginPage.input_field_password, LoginPage.input_value_password)

        self.click(LoginPage.submit_btn)

        self.assert_text("Index", "h1")

    def test_failed_login(self):
        self.send_keys(LoginPage.input_field_username, LoginPage.input_field_username)
        self.send_keys(LoginPage.input_field_password, LoginPage.input_value_invalid_password)

        self.click(LoginPage.submit_btn)
