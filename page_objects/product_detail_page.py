from seleniumbase import BaseCase


class ProductDetailPage(BaseCase):
    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    input_value_invalid_username = "ProductManager"
    input_value_invalid_password = "passProduct"
    submit_btn = "//input[@type='submit' and @value='Submit']"

    obsolete_btn = "//input[@value='Obsolete' and @class= 'btn btn-primary']"

    def open_page(self):
        self.get("https://localhost:44323/Product/ProductDetail/1")
