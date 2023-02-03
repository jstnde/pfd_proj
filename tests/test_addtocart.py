from page_objects.login_page import loginpage
class addtocart_Test(loginpage):
    def setUp(self,masterqa_mode=False):
        super().setUp()
        self.open_page()
        self.type(loginpage.input_field_username, loginpage.input_normaluser)
        self.type(loginpage.input_field_password, loginpage.input_password)

        self.click(loginpage.login_btn)

    def test_addtocart(self):
        print("Test case : add to cart successful")
        print("1. click on first item with backpack")
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        print("2. check the cart for previously added item")
        self.assert_text("YOUR CART", "span.title")
        self.assert_text("Backpack", "div.cart_item")
        self.save_screenshot("add_tocart",
                             loginpage.custom_screenshot_dir +
                             "/test_addtocart_product")
        print("Results: ")
        print("Cart has the previously added item")
        print("test is successful")
        self.save_screenshot_to_logs()


    def test_delete_cart(self):
        print("Test case : delete item from cart")
        print("1. add item to cart")
        self.click('button[name*="backpack"]')
        print("2. click into cart")
        self.click("#shopping_cart_container a")
        print("3. delete item from cart")
        self.click("button#remove-sauce-labs-backpack")
        self.save_screenshot("delete_from_tocart",
                             loginpage.custom_screenshot_dir +
                             "/test_addtocart_product")
        print("4. click 'continue shopping' button")
        self.click("button#continue-shopping")

        self.assert_text("ADD TO CART","button#add-to-cart-sauce-labs-backpack")
        print("Results : ")
        print("The button should change from 'REMOVE ITEM' to 'ADD TO CART'")
        print("test is successful")
        self.save_screenshot_to_logs()




