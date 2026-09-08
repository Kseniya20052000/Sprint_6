from allure import step
from locators import FAQPageLocators
from pages.base_page import BasePage


class FAQPage(BasePage):

    @step("Проверяю, что раздел FAQ отображается на странице")
    def is_faq_section_displayed(self):
        return self.is_displayed(FAQPageLocators.FAQ_SECTION)

    # --- Вопрос 1 ---

    @step("Кликаю на первый вопрос FAQ через JS (с прокруткой)")
    def click_question_1(self):
        button = self.find_visible(FAQPageLocators.QUESTION_1_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Получаю текст ответа на первый вопрос FAQ")
    def get_answer_1_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_1_TEXT)
        except Exception:
            return ""

    # --- Вопрос 2 ---

    @step("Кликаю на второй вопрос FAQ через JS (с прокруткой)")
    def click_question_2(self):
        button = self.find_visible(FAQPageLocators.QUESTION_2_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли второй вопрос FAQ (по aria-expanded)")
    def is_second_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_2_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на второй вопрос FAQ")
    def get_answer_2_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_2_TEXT)
        except Exception:
            return ""

    # --- Вопрос 3 ---

    @step("Кликаю на третий вопрос FAQ через JS (с прокруткой)")
    def click_question_3(self):
        button = self.find_visible(FAQPageLocators.QUESTION_3_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли третий вопрос FAQ (по aria-expanded)")
    def is_third_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_3_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на третий вопрос FAQ")
    def get_answer_3_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_3_TEXT)
        except Exception:
            return ""

    # --- Вопрос 4 ---

    @step("Кликаю на четвёртый вопрос FAQ через JS (с прокруткой)")
    def click_question_4(self):
        button = self.find_visible(FAQPageLocators.QUESTION_4_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли четвёртый вопрос FAQ (по aria-expanded)")
    def is_fourth_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_4_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на четвёртый вопрос FAQ")
    def get_answer_4_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_4_TEXT)
        except Exception:
            return ""

    # --- Вопрос 5 ---

    @step("Кликаю на пятый вопрос FAQ через JS (с прокруткой)")
    def click_question_5(self):
        button = self.find_visible(FAQPageLocators.QUESTION_5_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли пятый вопрос FAQ (по aria-expanded)")
    def is_fifth_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_5_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на пятый вопрос FAQ")
    def get_answer_5_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_5_TEXT)
        except Exception:
            return ""

    # --- Вопрос 6 ---

    @step("Кликаю на шестой вопрос FAQ через JS (с прокруткой)")
    def click_question_6(self):
        button = self.find_visible(FAQPageLocators.QUESTION_6_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли шестой вопрос FAQ (по aria-expanded)")
    def is_sixth_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_6_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на шестой вопрос FAQ")
    def get_answer_6_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_6_TEXT)
        except Exception:
            return ""

    # --- Вопрос 7 ---

    @step("Кликаю на седьмой вопрос FAQ через JS (с прокруткой)")
    def click_question_7(self):
        button = self.find_visible(FAQPageLocators.QUESTION_7_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли седьмой вопрос FAQ (по aria-expanded)")
    def is_seventh_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_7_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на седьмой вопрос FAQ")
    def get_answer_7_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_7_TEXT)
        except Exception:
            return ""

    # --- Вопрос 8 ---

    @step("Кликаю на восьмой вопрос FAQ через JS (с прокруткой)")
    def click_question_8(self):
        button = self.find_visible(FAQPageLocators.QUESTION_8_BUTTON)
        self.scroll_to_element(button)
        self.click_js(button)

    @step("Проверяю, раскрыт ли восьмой вопрос FAQ (по aria-expanded)")
    def is_eighth_question_expanded(self):
        try:
            return self.get_attribute(FAQPageLocators.QUESTION_8_BUTTON, "aria-expanded") == "true"
        except Exception:
            return False

    @step("Получаю текст ответа на восьмой вопрос FAQ")
    def get_answer_8_text(self):
        try:
            return self.get_text(FAQPageLocators.ANSWER_8_TEXT)
        except Exception:
            return ""
