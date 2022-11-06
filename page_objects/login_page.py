from seleniumbase import BaseCase


class LoginPage(BaseCase):
    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    submit_btn = "//input[@type='submit' and @value='Submit']"

    input_value_invalid_password = "abc"

    def open_page(self):
        self.open("https://localhost:44323")
