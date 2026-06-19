from .base_page import BasePage
from ..locators.cookie_locators import Cookie
from ..locators.faq_locators import FAQ
import allure


class FaqQuestions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cookie_button = Cookie.COOKIE
        self.question_1 = FAQ.QUESTION_1
        self.answer_1 = FAQ.ANSWER_1
        self.question_2 = FAQ.QUESTION_2
        self.answer_2 = FAQ.ANSWER_2
        self.question_3 = FAQ.QUESTION_3
        self.answer_3 = FAQ.ANSWER_3
        self.question_4 = FAQ.QUESTION_4
        self.answer_4 = FAQ.ANSWER_4
        self.question_5 = FAQ.QUESTION_5
        self.answer_5 = FAQ.ANSWER_5
        self.question_6 = FAQ.QUESTION_6
        self.answer_6 = FAQ.ANSWER_6
        self.question_7 = FAQ.QUESTION_7
        self.answer_7 = FAQ.ANSWER_7
        self.question_8 = FAQ.QUESTION_8
        self.answer_8 = FAQ.ANSWER_8

    @allure.step("Принять куки")
    def click_cookie(self):
        self.click(self.cookie_button)

    def _click_question(self, question_locator, answer_locator):
        self.click_and_wait_for_element(question_locator, answer_locator)

    def _get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step("Раскрытие первого вопроса")
    def click_questions1_in_button(self):
        self._click_question(self.question_1, self.answer_1)

    def answer1(self):
        return self._get_answer_text(self.answer_1)

    @allure.step("Раскрытие второго вопроса")
    def click_questions2_in_button(self):
        self._click_question(self.question_2, self.answer_2)

    def answer2(self):
        return self._get_answer_text(self.answer_2)

    @allure.step("Раскрытие третьего вопроса")
    def click_questions3_in_button(self):
        self._click_question(self.question_3, self.answer_3)

    def answer3(self):
        return self._get_answer_text(self.answer_3)

    @allure.step("Раскрытие четвертого вопроса")
    def click_questions4_in_button(self):
        self._click_question(self.question_4, self.answer_4)

    def answer4(self):
        return self._get_answer_text(self.answer_4)

    @allure.step("Раскрытие пятого вопроса")
    def click_questions5_in_button(self):
        self._click_question(self.question_5, self.answer_5)

    def answer5(self):
        return self._get_answer_text(self.answer_5)

    @allure.step("Раскрытие шестого вопроса")
    def click_questions6_in_button(self):
        self._click_question(self.question_6, self.answer_6)

    def answer6(self):
        return self._get_answer_text(self.answer_6)

    @allure.step("Раскрытие седьмого вопроса")
    def click_questions7_in_button(self):
        self._click_question(self.question_7, self.answer_7)

    def answer7(self):
        return self._get_answer_text(self.answer_7)

    @allure.step("Раскрытие восьмого вопроса")
    def click_questions8_in_button(self):
        self._click_question(self.question_8, self.answer_8)

    def answer8(self):
        return self._get_answer_text(self.answer_8)
    