from seleniumbase import BaseCase


class CreateProductPage(BaseCase):
    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    input_value_invalid_username = "ProductManager"
    input_value_invalid_password = "passProduct"
    submit_btn = "//input[@type='submit' and @value='Submit']"

    def open_page(self):
        self.open("https://localhost:44323")

    def login(self):
        self.open_page()
        self.send_keys(self.input_field_username, self.input_value_username)
        self.send_keys(self.input_field_password, self.input_value_password)
        self.click(self.submit_btn)
