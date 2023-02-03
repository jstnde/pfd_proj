from seleniumbase import BaseCase
from datetime import datetime
class checkoutpage(BaseCase):

    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "customer_screenshots/"+\
                            datetime.now().strftime(datetime_format) + "/product_page"

    #login information
    input_field_username = "input#user-name"
    input_field_password = "input#password"
    login_btn = "input#login-button"
    input_password = "secret_sauce"
    input_normaluser = "standard_user"

    #checkout_information
    input_firstname = "input#first-name"
    input_lastname = "input#last-name"
    input_postalcode = "input#postal-code"
    firstname = "seleniumbase"
    lastname = "automation"
    postalcode = "77123"


    def open_page(self):
        self.open("https://www.saucedemo.com/")