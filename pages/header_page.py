from pages.base_page import BasePage
from allure import step
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    # locators
    order_button_top = [
        By.XPATH,
        ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button')]",
    ]
    samokat_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]

    # methods
    def __init__(self, driver):
        super().__init__(driver)

    @step("Загрузка элементов хэдера")
    def wait_for_page_loaded(self):
        self.wait_for_element(self.order_button_top)

    @step("Переход к заказу через верхнюю кнопку")
    def go_to_order_by_top_button(self):
        self.click_element(self.order_button_top)

    @step("переход на главную через лого")
    def go_main_page(self):
        self.click_element(self.samokat_logo)

    @step("Открытие Яндекс Дзен по клику на лого")
    def open_yandex_dzen(self):
        self.click_element(self.yandex_logo)
