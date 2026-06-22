import src.data as data
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.header_page import HeaderPage


class TestMakeOrder:
    @pytest.mark.parametrize(
        "order_button, order_data",
        [("top", data.ORDER_DATA[0]), ("down", data.ORDER_DATA[1])],
        ids=["top_button", "down_button"],
    )
    def test_make_order(self, driver, order_data, order_button):

        main_page = MainPage(driver)
        main_page.get_url(data.DEFAULT_URL)

        header = HeaderPage(driver)
        header.wait_for_page_loaded()

        if order_button == "top":
            header.go_to_order_by_top_button()
        else:
            main_page.go_to_order_by_down_button()

        order_page = OrderPage(driver)

        order_page.fill_order_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"],
            order_data["date"],
            order_data["duration"],
            order_data["color"],
            order_data["comment"],
        )

        order_page.go_order_status_page()

        header.go_main_page()
        assert main_page.get_current_url() == data.DEFAULT_URL

        header.open_yandex_dzen()

        main_page.switch_window(data.DZEN_PAGE_TITLE)

        assert main_page.get_current_url() == data.DZEN_PAGE_URL
