from page_objects.create_product_page import CreateProductPage


class CreateProductTest(CreateProductPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.login()
        self.click_link(CreateProductPage.a_create)

    # Test Case 2 : Create Product
    def test_create_product(self):
        file_path = "./data/logo.jpg"

        self.choose_file(CreateProductPage.input_field_file, file_path)
        self.send_keys(CreateProductPage.input_field_title, CreateProductPage.input_value_title)
        self.send_keys(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        self.click(CreateProductPage.submit_btn)

        self.assert_text(CreateProductPage.expected_page_title, CreateProductPage.page_title)

