from page_objects.login_page import loginpage
class loginTest(loginpage):

    def setUp(self,masterqa_mode=False):
        super().setUp()
        self.open("https://www.saucedemo.com/")

    # Test case 1 : unsuccessful login(wrong email)
    def test_login_wrong(self):
        print("Test case : unsuccessful login (user is locked out)")
        print("1. input wrong username : 'locked_out_user'")
        self.type(loginpage.input_field_username, loginpage.input_wronguser)
        print("2. input password: 'secret_sauce'")
        self.type(loginpage.input_field_password, loginpage.input_password)
        self.save_screenshot("unsuccessful_login", loginpage.custom_screenshot_dir+
                             "/test_login_error_msg")

        self.click(loginpage.login_btn)
        self.assert_true(self.is_text_visible(loginpage.error_msg, "h3"))
        print("results: ")
        print("Error message appears")
        print("test is successful")
        self.save_screenshot_to_logs()

    # Test case 2 : successful login

    def test_login_correct(self):
        print("Test case : successful login")
        print("1. input correct username : 'standard_user' ")
        self.type(loginpage.input_field_username, loginpage.input_normaluser)
        print("2. input correct password : 'secret_sauce' ")
        self.type(loginpage.input_field_password, loginpage.input_password)

        self.click(loginpage.login_btn)
        self.save_screenshot("Successful_login", loginpage.custom_screenshot_dir +
                             "/test_login")
        print("Page should redirect")
        self.assert_text("PRODUCTS", "span.title")
        print("results : ")
        print("user is being redirected")
        print("test is successful")
        self.save_screenshot_to_logs()



