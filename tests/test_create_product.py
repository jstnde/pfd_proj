from page_objects.create_product_page import CreateProductPage


class CreateProductTest(CreateProductPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.login()
        self.click_link("Create Product")

    # Test Case 2 : Create Product
    def test_create_product(self):
        file_path = "./data/logo.jpg"

        self.choose_file("#filetoupload", file_path)
        self.send_keys("#ProductTitle", "Bottom Baggy Jeans")
        self.send_keys("#price", "59.99")

        self.click("//input[@type='submit']")

        self.assert_title("View Products - WEB2022APR_P05_T2")

