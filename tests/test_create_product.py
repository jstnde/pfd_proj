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

        # TODO: print log here

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        # TODO: print log here

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        # TODO: print log here

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

        # TODO: print log here

        # TODO:
        #  exception handling

    # Test Case 4 : Image Upload Validation
    def test_image_validation(self):
        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        # TODO: print log here

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        # TODO: print log here

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_image_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_image_validation")

        self.click(CreateProductPage.submit_btn)

        # TODO:
        #  add assertion
        #  exception handling

    # Test Case 5 : Title Field Validation
    def test_title_validation(self):
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        # TODO: print log here

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        # TODO: print log here

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        self.click(CreateProductPage.submit_btn)

        # TODO:
        #  add assertion
        #  exception handling

    # Test Case 6 : Price Field Validation
    def test_price_validation(self):
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        # TODO: print log here

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        # TODO: print log here

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        self.click(CreateProductPage.submit_btn)

        # TODO:
        #  add assertion
        #  exception handling
