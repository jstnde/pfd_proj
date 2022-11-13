from seleniumbase import BaseCase
from datetime import datetime


class ProductDetailPage(BaseCase):
    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "custom_screenshots/" + \
                            datetime.now().strftime(datetime_format) + \
                            "/product_detail_page"

    submit_btn = "//input[@type='submit']"
    a_update = "Update Details"
    title_field = "#ProductTitle"
    title_value = "Pretty outfit 2"
    price_field = "#Price"
    price_value = 420

    js_footer_hide = "document.getElementsByClassName('container')[2].hidden = true"
    obsolete_btn = "//input[@value='Obsolete' and @class= 'btn btn-primary']"
    effective_field = "#date"
    expected_style = "background-color: red; color: white;"

    def open_page(self):
        self.get("https://localhost:44323/Product")
