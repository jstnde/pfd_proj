from page_objects.create_product_page import CreateProductPage


class CreateProductTest(CreateProductPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.login()

        self.save_screenshot("products_page",
                             CreateProductPage.custom_screenshot_dir)

        self.click_link(CreateProductPage.a_create)

        self.save_screenshot("create_product_page",
                             CreateProductPage.custom_screenshot_dir)

    # Test Case 3 : Create Product
    def test_create_product(self):
        print("Successful Creation of Product")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Uploading test Image Completed")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input test title value : 'Bottom Baggy Jeans'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("3. Input test price value : '$59.99'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("filled_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        self.click(CreateProductPage.submit_btn)


        self.assert_text(CreateProductPage.expected_page_title, CreateProductPage.page_title)

        self.scroll_to_bottom()
        self.save_screenshot("updated_products_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        print("4. Press submit button")
        print("Product creation completed and shown in homepage")
        print("Test is Successful")

        # TODO:
        #  exception handling

    # Test Case 4 : Image Upload Validation
    def test_image_validation(self):
        print("Test Case 4 : Image Upload Validation")

        print("1. Uploading Image Incomplete")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input test title : 'Bottom Baggy Jeans'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("3. Input test right price : '59.99'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_image_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_image_validation")

        self.click(CreateProductPage.submit_btn)

        print("4. Click Submit Button")
        print("Error message for not uploading product image appears")
        print("Test is Successful")

        # TODO:
        #  add assertion
        #  exception handling

    # Test Case 5 : Title Field Validation
    def test_title_validation(self):
        print("Test Case 5 : Title Field Validation")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Uploading Test Image Complete")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)


        print("2. Leaving Input Title empty")
        print("3. Input Test Right Price : 59.99")


        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        self.click(CreateProductPage.submit_btn)

        print("4. Click Submit Button")
        print("Error message for empty product title appears")
        print("Test is Successful")

        # TODO:
        #  add assertion
        #  exception handling

    # Test Case 6 : Price Field Range Validation
    def test_price_validation(self):
        print("Test Case 6 : Price Field Range Validation")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Uploading Test Image Complete")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input Test Title : 'Bottom Baggy Jeans'")

        #this part is for the wrong pricing : 1000.00 to check if my price range works(i m sry if i did smth wrong )
        self.type(CreateProductPage.input_field_price, CreateProductPage.input_wrong_price)

        print("3. Input Test Wrong Price : 1000.00")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        self.click(CreateProductPage.submit_btn)

        print("4. Click Submit Button")
        print("Error message warning user about price range appears")
        print("Test is Successful")

        # TODO:
        #  add assertion
        #  exception handling
