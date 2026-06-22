import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    # locators

    name_input = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_select = [By.CSS_SELECTOR, "input.select-search__input"]
    phone_input = [
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    ]
    next_button = [
        By.XPATH,
        ".//div[contains(@class, 'Order_NextButton')]/button[text()='Далее']",
    ]

    when_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    time_input = [By.CSS_SELECTOR, "span.Dropdown-arrow"]
    comment_input = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    order_final_button = [
        By.XPATH,
        ".//div[contains(@class, 'Order_Buttons')]/button[contains(@class, 'Button_Button') and text()='Заказать']",
    ]
    order_yes_button = [
        By.XPATH,
        ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_Buttons')]/button[contains(@class, 'Button_Button') and text()='Да']",
    ]
    order_complete_modal = [
        By.XPATH,
        ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']",
    ]
    order_status_button = [
        By.XPATH,
        ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_NextButton')]/button",
    ]

    def click_metro_option(self, metro_name):
        self.click_element(
            (
                By.XPATH,
                f".//div[@class='select-search__select']/ul/li/button/div[contains(@class, 'Order_Text') and text()='{metro_name}']",
            )
        )

    def click_time_option(self, time_text):
        self.click_element(
            (
                By.XPATH,
                f".//div[contains(@class, 'Dropdown-option') and text()='{time_text}']",
            )
        )

    def choose_color_option(self, color):
        self.click_element(
            (
                By.XPATH,
                f".//label[contains(@class, 'Checkbox_Label') and @for='{color}']",
            )
        )

    # methods
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение формы заказа")
    def fill_order_form(
        self, name, surname, address, metro, phone, date, duration, color, comment
    ):
        self.enter_text(self.name_input, name)
        self.enter_text(self.surname_input, surname)
        self.enter_text(self.address_input, address)
        self.enter_text(self.metro_select, metro)
        self.click_metro_option(metro)
        self.enter_text(self.phone_input, phone)
        self.click_element(self.next_button)
        self.enter_text(self.when_input, date)
        self.click_element(self.time_input)
        self.click_time_option(duration)
        self.choose_color_option(color)
        self.enter_text(self.comment_input, comment)
        self.click_element(self.order_final_button)
        self.click_element(self.order_yes_button)

        assert self.wait_for_element(self.order_complete_modal), (
            "Сбой при создании заказа"
        )

    @allure.step("Переход к статусу заказа")
    def go_order_status_page(self):
        self.click_element(self.order_status_button)
