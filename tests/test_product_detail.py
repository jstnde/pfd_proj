from seleniumbase import BaseCase


class ProductDetailTest(BaseCase):
    # Test Case 4 : Obsolete Button
    def test_obsolete_button(self):
        self.get("https://localhost:44323/Product/ProductDetail/1")