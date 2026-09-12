import allure
from locators import FAQPageLocators
from pages.base_page import BasePage


class FAQPage(BasePage):

    @allure.step("Проверяет, что раздел FAQ отображается")
    def is_faq_section_displayed(self):
        return self.is_displayed(FAQPageLocators.FAQ_SECTION, timeout=10)

    @allure.step("Кликает на вопрос по индексу")
    def click_question_by_index(self, index: int):
        locator = (
            FAQPageLocators.QUESTION_BUTTON[0],
            FAQPageLocators.QUESTION_BUTTON[1].format(index)
        )
        self.click(locator)

    @allure.step("Проверяет, раскрыт ли вопрос по индексу")
    def is_question_expanded(self, index: int) -> bool:
        locator = (
            FAQPageLocators.QUESTION_BUTTON[0],
            FAQPageLocators.QUESTION_BUTTON[1].format(index)
        )
        return self.driver.find_element(*locator).get_attribute("aria-expanded") == "true"

    @allure.step("Получает текст ответа по индексу вопроса")
    def get_answer_text_by_index(self, index: int) -> str:
        locator = (
            FAQPageLocators.ANSWER_PANEL[0],
            FAQPageLocators.ANSWER_PANEL[1].format(index)
        )
        return self.driver.find_element(*locator).text