from page_objects.product_detail_page import ProductDetailPage


class ProductDetailTest(ProductDetailPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.open_page()

    # Test Case 4 : Obsolete Button
    def test_obsolete_button(self):
        self.click(ProductDetailPage.obsolete_btn)
        self.open_page()
