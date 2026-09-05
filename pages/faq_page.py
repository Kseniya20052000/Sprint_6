from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import FAQPageLocators


class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_faq_section_displayed(self):
        """Проверяет отображение раздела FAQ"""
        section = self.wait.until(
            EC.visibility_of_element_located(FAQPageLocators.FAQ_SECTION)
        )
        return section.is_displayed()

    # --- Вопрос 1 ---

    def click_question_1(self):
        """Кликает на первый вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(
            EC.visibility_of_element_located(FAQPageLocators.QUESTION_1_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_answer_1_text(self):
        """Получает текст ответа на первый вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_1_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 2 ---

    def click_question_2(self):
        """Кликает на второй вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_2_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_second_question_expanded(self):
        """Проверяет, раскрыт ли второй вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_2_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_2_text(self):
        """Получает текст ответа на второй вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_2_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 3 ---

    def click_question_3(self):
        """Кликает на третий вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_3_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_third_question_expanded(self):
        """Проверяет, раскрыт ли третий вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_3_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_3_text(self):
        """Получает текст ответа на третий вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_3_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 4 ---

    def click_question_4(self):
        """Кликает на четвёртый вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_4_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_fourth_question_expanded(self):
        """Проверяет, раскрыт ли четвёртый вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_4_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_4_text(self):
        """Получает текст ответа на четвёртый вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_4_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 5 ---

    def click_question_5(self):
        """Кликает на пятый вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_5_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_fifth_question_expanded(self):
        """Проверяет, раскрыт ли пятый вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_5_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_5_text(self):
        """Получает текст ответа на пятый вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_5_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 6 ---

    def click_question_6(self):
        """Кликает на шестой вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_6_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_sixth_question_expanded(self):
        """Проверяет, раскрыт ли шестой вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_6_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_6_text(self):
        """Получает текст ответа на шестой вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_6_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 7 ---

    def click_question_7(self):
        """Кликает на седьмой вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_7_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_seventh_question_expanded(self):
        """Проверяет, раскрыт ли седьмой вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_7_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_7_text(self):
        """Получает текст ответа на седьмой вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_7_TEXT))
            return answer.text
        except Exception:
            return ""

    # --- Вопрос 8 ---

    def click_question_8(self):
        """Кликает на восьмой вопрос через JS после прокрутки к элементу"""
        button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_8_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_eighth_question_expanded(self):
        """Проверяет, раскрыт ли восьмой вопрос (по атрибуту aria-expanded)"""
        try:
            button = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.QUESTION_8_BUTTON))
            expanded_attr = button.get_attribute("aria-expanded")
            return expanded_attr == "true"
        except Exception:
            return False

    def get_answer_8_text(self):
        """Получает текст ответа на восьмой вопрос"""
        try:
            answer = self.wait.until(EC.visibility_of_element_located(FAQPageLocators.ANSWER_8_TEXT))
            return answer.text
        except Exception:
            return ""
