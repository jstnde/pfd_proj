from page_objects.product_detail_page import ProductDetailPage


class ProductDetailTest(ProductDetailPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.open_page()


    # Test Case 3 : Edit Product
    def test_edit_product(self):
        self.click_link(ProductDetailPage.a_update)
        self.clear(ProductDetailPage.title_field)
        self.send_keys(ProductDetailPage.title_field, ProductDetailPage.title_value)
        self.clear(ProductDetailPage.price_field)
        self.send_keys(ProductDetailPage.price_field, ProductDetailPage.price_value)
        self.click(ProductDetailPage.submit_btn)

        self.open_page()
        self.assert_text(ProductDetailPage.title_value, ProductDetailPage.title_field)
        self.assert_text(ProductDetailPage.price_value, ProductDetailPage.price_field)



    # Test Case 4 : Obsolete Button
    def test_obsolete_button(self):
        self.add_js_code(ProductDetailPage.js_footer_hide)

        self.click(ProductDetailPage.obsolete_btn)
        self.open_page()
        self.assert_attribute(ProductDetailPage.effective_field, "style", ProductDetailPage.expected_style)
