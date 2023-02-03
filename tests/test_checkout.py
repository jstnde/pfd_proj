from page_objects.checkout_page import checkoutpage
class checkout_Test(checkoutpage):
    def setUp(self,masterqa_mode=False):
        super().setUp()
        self.open_page()
        self.type(checkoutpage.input_field_username, checkoutpage.input_normaluser)
        self.type(checkoutpage.input_field_password, checkoutpage.input_password)

        self.click(checkoutpage.login_btn)
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.click("button#checkout")


    def test_checkout_unsuccessful_firstnameblank(self):
        print("Test case : checkout first name leave blank")
        print("1. Enter last name : 'automation'")
        self.type(checkoutpage.input_lastname, checkoutpage.lastname)
        print("2. Enter postal code : '77123'")
        self.type(checkoutpage.input_postalcode, checkoutpage.postalcode)
        print("3. Click continue")
        self.click("input#continue")
        print("Error message should appear")
        self.assert_text("Error: First Name is required", "h3")
        self.save_screenshot("checkout_firstname_error",
                             checkoutpage.custom_screenshot_dir +
                             "/test_checkout_product")
        print("Results : ")
        print("Error message : 'first name is required' appeared")
        print("test is successful")
        self.save_screenshot_to_logs()

    def test_checkout_unsuccessful_lastnameblank(self):
        print("Test case : checkout last name leave blank")
        print("1. Enter first name : 'seleniumbase'")
        self.type(checkoutpage.input_firstname, checkoutpage.firstname)
        print("2. Enter postal code : '77123'")
        self.type(checkoutpage.input_postalcode, checkoutpage.postalcode)
        print("3. Click continue")
        self.click("input#continue")
        print("Error message should appear")
        self.assert_text("Error: Last Name is required", "h3")
        self.save_screenshot("checkout_lastname_error",
                             checkoutpage.custom_screenshot_dir +
                             "/test_checkout_product")
        print("Results : ")
        print("Error message : 'last name is required' appeared")
        print("test is successful")
        self.save_screenshot_to_logs()

    def test_checkout_unsuccessful_postalcodeblank(self):
        print("Test case : checkout postal code leave blank")
        print("1. Enter first name : 'seleniumbase'")
        self.type(checkoutpage.input_firstname, checkoutpage.firstname)
        print("2. Enter last name : 'automation'")
        self.type(checkoutpage.input_lastname, checkoutpage.lastname)
        print("3. Click continue")
        self.click("input#continue")
        print("Error message should appear")
        self.assert_text("Error: Postal Code is required", "h3")
        self.save_screenshot("checkout_postalcode_error",
                             checkoutpage.custom_screenshot_dir +
                             "/test_checkout_product")
        print("Results : ")
        print("Error message : 'Postal code is required' appeared")
        print("test is successful")
        self.save_screenshot_to_logs()

    def test_checkout_successful(self):
        print("Test case : checkout successful")
        print("1. Enter first name : 'seleniumbase'")
        self.type(checkoutpage.input_firstname, checkoutpage.firstname)
        print("2. Enter last name : 'automation'")
        self.type(checkoutpage.input_lastname, checkoutpage.lastname)
        print("3. Enter postal code : '77123'")
        self.type(checkoutpage.input_postalcode, checkoutpage.postalcode)
        print("4. Click continue")
        self.click("input#continue")
        print("5. the user should be redirected to a next page")
        self.assert_text("CHECKOUT: OVERVIEW")
        print("6. Item is displayed in the page")
        self.assert_text("Backpack", "div.cart_item")
        print("7. Click finish")
        self.click("button#finish")
        print("8. Thank you message should appear")
        self.assert_exact_text("THANK YOU FOR YOUR ORDER", "h2")
        self.save_screenshot("checkout_successful",
                             checkoutpage.custom_screenshot_dir +
                             "/test_checkout_product")
        print("Results :")
        print("Thank you message appeared")
        print("test is successful")
        self.save_screenshot_to_logs()
