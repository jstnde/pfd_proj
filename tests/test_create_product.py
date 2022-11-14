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
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("Uploading test Image Completed")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("Input test title value : 'Bottom Baggy Jeans'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("Input test price value : '$59.99'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("filled_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        self.click(CreateProductPage.submit_btn)

        print("Press submit button")

        self.assert_text(CreateProductPage.expected_page_title, CreateProductPage.page_title)

        self.scroll_to_bottom()
        self.save_screenshot("updated_products_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        print("Product creation completed and shown in homepage")

        # TODO:
        #  exception handling

    # Test Case 4 : Image Upload Validation
    def test_image_validation(self):

        print("Uploading Image Incomplete")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("Input test title : 'Bottom Baggy Jeans'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("Input test right price : '59.99'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_image_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_image_validation")

        self.click(CreateProductPage.submit_btn)

        print("Click Submit Button")

        self.save_screenshot("error_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        print("Error message for not uploading product image appears")

        self.assert_title_contains("Create")

        # TODO:
        #  exception handling

    # Test Case 5 : Title Field Validation
    def test_title_validation(self):
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("Uploading Test Image Complete")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("Leaving Input Title empty")
        print("Input Test Right Price : 59.99")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        self.click(CreateProductPage.submit_btn)

        print("Click Submit Button")

        self.save_screenshot("error_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        print("Error message for empty product title appears")

        self.assert_title_contains("Create")

        # TODO:
        #  exception handling

    # Test Case 6 : Price Field Range Validation
    def test_price_validation(self):
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("Uploading Test Image Complete")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("Input Test Title : 'Bottom Baggy Jeans'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_wrong_price)

        print("Input Test Wrong Price : 1000.00")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("invalid_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        self.click(CreateProductPage.submit_btn)

        print("Click Submit Button")

        self.save_screenshot("error_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        print("Error message warning user about price range appears")

        self.assert_title_contains("Create")

        # TODO:
        #  exception handling
