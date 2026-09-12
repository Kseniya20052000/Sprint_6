import pytest
import allure

FAQ_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]


@allure.feature("FAQ Section")
class TestFAQQuestions:

    @allure.story("Проверка раскрытия всех вопросов и текстов ответов в FAQ")
    @pytest.mark.parametrize("question_index, expected_text", FAQ_DATA)
    @allure.title("FAQ: проверка раскрытия вопроса №{question_index} и текста ответа")
    def test_faq_question(self, faq_page, question_index, expected_text):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел не отображается"

        with allure.step(f"Клик на вопрос №{question_index + 1}"):
            faq_page.click_question_by_index(question_index)

        with allure.step(f"Проверка, что вопрос №{question_index + 1} раскрылся"):
            assert faq_page.is_question_expanded(question_index), "Вопрос не раскрылся"

        with allure.step(f"Проверка текста ответа для вопроса №{question_index + 1}"):
            actual_text = faq_page.get_answer_text_by_index(question_index)
            assert expected_text in actual_text, (
                f"Ожидаемый текст не найден.\nОжидался: '{expected_text}'\nПолучен: '{actual_text}'"
            )
