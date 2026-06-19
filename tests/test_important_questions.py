import allure
import pytest
from ..pages.important_questions_pages import FaqQuestions
from ..data.faq_data import FAQ_ANSWERS

@allure.feature("Вопросы о важном")
class TestFAQ:

    @pytest.mark.parametrize("faq_data", FAQ_ANSWERS)
    @allure.title("Проверка открытия ответа на вопрос FAQ: {faq_data[expected_text]}") 
    @allure.description("При клике на вопрос должен открываться соответствующий текст ответа")
    def test_faq_questions(self, driver, faq_data):
        faq = FaqQuestions(driver)

        faq.click_cookie()

        question_method_name = faq_data["question_method"]
        answer_method_name = faq_data["answer_method"]
        expected_text = faq_data["expected_text"]

        getattr(faq, question_method_name)()

        answer_text = getattr(faq, answer_method_name)()

        assert answer_text == expected_text, (
            f"Ошибка в тесте для вопроса '{question_method_name}'.\n"
            f"Ожидаемый текст:\n'{expected_text}'\n"
            f"Фактический текст:\n'{answer_text}'"
        )
