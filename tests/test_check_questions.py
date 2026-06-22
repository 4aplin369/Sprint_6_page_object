import src.data as data
import pytest

from pages.main_page import MainPage


class TestCheckQuestions:
    @pytest.mark.parametrize("number", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_questions(self, driver, number):

        main_page = MainPage(driver)
        main_page.get_url(data.DEFAULT_URL)
        main_page.wait_for_page_loaded()

        main_page.check_question_text(number)
