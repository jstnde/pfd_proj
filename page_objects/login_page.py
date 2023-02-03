from seleniumbase import BaseCase
from datetime import datetime
class loginpage(BaseCase):
    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "customer_screenshots/"+\
                            datetime.now().strftime(datetime_format) + "/register_page"

    input_field_username = "input#user-name"
    input_field_password = "input#password"
    login_btn = "input#login-button"
    input_password = "secret_sauce"

    input_normaluser = "standard_user"
    input_wronguser = "locked_out_user"

    error_msg = "Epic sadface: Sorry, this user has been locked out."
    error_span = "h3"
    error_style = "color:red"
    def open_page(self):
        self.open("https://www.saucedemo.com/")
