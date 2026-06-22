import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step("Перейти по")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("Проверка текущего урла")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание элементов")
    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Клик по элементу")
    def click_element(self, locator, timeout=10):
        self.wait_for_element(locator, timeout).click()

    @allure.step("Ввод текста")
    def enter_text(self, locator, text, timeout=10):
        self.wait_for_element(locator, timeout).send_keys(text)

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключение вкладки")
    def switch_window(self, title):

        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        wait.until(EC.title_contains(title))
