from seleniumbase import BaseCase


class CreateProductPage(BaseCase):
    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    submit_btn = "//input[@type='submit' and @value='Submit']"

    def open_page(self):
        self.open("https://localhost:44323")

    def login(self):
        self.open_page()
        self.send_keys("input#uname", "ProductManager")
        self.send_keys("input#upass", "passProduct")
        self.click("//input[@type='submit' and @value='Submit']")
