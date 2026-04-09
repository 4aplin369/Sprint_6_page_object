import src.data as data

from pages.base_page import BasePage
from allure import step
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # locators
    questions_block = [By.CSS_SELECTOR, "div.accordion"]
    order_button_top = [
        By.XPATH,
        ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button')]",
    ]
    order_button_down = [
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Middle') and text()='Заказать']",
    ]

    def get_question_by_number(self, number):
        question = [
            By.XPATH,
            f".//div[@id='accordion__heading-{number}' and @class='accordion__button']",
        ]
        return question

    def get_answer_by_number(self, number):
        answer = [By.XPATH, f".//div[@id='accordion__panel-{number}']"]

        return answer

    # methods
    def __init__(self, driver):
        super().__init__(driver)

    @step("Открыть главную страницу")
    def open_page(self):
        self.get_url(data.DEFAULT_URL)

    @step("Загрузка элементов главной страницы")
    def wait_for_page_loaded(self):
        self.wait_for_element(self.questions_block)

    @step("Проверка текстов ответов на вопросы")
    def check_question_text(self, question_number):
        self.scroll_to_element(self.get_question_by_number(question_number))
        self.click_element(self.get_question_by_number(question_number))

        assert (
            self.wait_for_element(self.get_answer_by_number(question_number)).text
            == data.QUESTION_TEXTS[question_number]
        )

    @step("Переход к заказу через нижнюю кнопку")
    def go_to_order_by_down_button(self):
        self.scroll_to_element(self.order_button_down)
        self.click_element(self.order_button_down)
