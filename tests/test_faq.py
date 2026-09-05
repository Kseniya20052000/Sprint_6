import allure


@allure.feature("FAQ Section")
class TestFAQQuestions:

    @allure.story("Проверка раскрытия текста первого вопроса")
    @allure.title("Вопрос 1: Сколько это стоит? И как оплатить?")
    def test_faq_question_1(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на первый вопрос"):
            faq_page.click_question_1()

        with allure.step("Проверка текста ответа"):
            expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
            actual_text = faq_page.get_answer_1_text()
            assert expected_text in actual_text, f"Ожидаемый текст: '{expected_text}', но получен: '{actual_text}'"

    @allure.story("Проверка раскрытия текста второго вопроса")
    @allure.title("Вопрос 2: Хочу сразу несколько самокатов! Так можно?")
    def test_faq_question_2(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на второй вопрос"):
            faq_page.click_question_2()

        with allure.step("Проверка раскрытия текста второго вопроса"):
            assert faq_page.is_second_question_expanded(), "Текст второго вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_2_text()
            expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста третьего вопроса")
    @allure.title("Вопрос 3: Как рассчитывается время аренды?")
    def test_faq_question_3(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на третий вопрос"):
            faq_page.click_question_3()

        with allure.step("Проверка раскрытия текста третьего вопроса"):
            assert faq_page.is_third_question_expanded(), "Текст третьего вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_3_text()
            expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста четвёртого вопроса")
    @allure.title("Вопрос 4: Можно ли заказать самокат прямо на сегодня?")
    def test_faq_question_4(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на четвёртый вопрос"):
            faq_page.click_question_4()

        with allure.step("Проверка раскрытия текста четвёртого вопроса"):
            assert faq_page.is_fourth_question_expanded(), "Текст четвёртого вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_4_text()
            expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста пятого вопроса")
    @allure.title("Вопрос 5: Можно ли продлить заказ или вернуть самокат раньше?")
    def test_faq_question_5(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на пятый вопрос"):
            faq_page.click_question_5()

        with allure.step("Проверка раскрытия текста пятого вопроса"):
            assert faq_page.is_fifth_question_expanded(), "Текст пятого вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_5_text()
            expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста шестого вопроса")
    @allure.title("Вопрос 6: Вы привозите зарядку вместе с самокатом?")
    def test_faq_question_6(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на шестой вопрос"):
            faq_page.click_question_6()

        with allure.step("Проверка раскрытия текста шестого вопроса"):
            assert faq_page.is_sixth_question_expanded(), "Текст шестого вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_6_text()
            expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста седьмого вопроса")
    @allure.title("Вопрос 7: Можно ли отменить заказ?")
    def test_faq_question_7(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на седьмой вопрос"):
            faq_page.click_question_7()

        with allure.step("Проверка раскрытия текста седьмого вопроса"):
            assert faq_page.is_seventh_question_expanded(), "Текст седьмого вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_7_text()
            expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"

    @allure.story("Проверка раскрытия текста восьмого вопроса")
    @allure.title("Вопрос 8: Я живу за МКАДом, привезёте?")
    def test_faq_question_8(self, faq_page):
        with allure.step("Проверка отображения раздела «Вопросы о важном»"):
            assert faq_page.is_faq_section_displayed(), "Раздел «Вопросы о важном» не отображается"

        with allure.step("Клик на восьмой вопрос"):
            faq_page.click_question_8()

        with allure.step("Проверка раскрытия текста восьмого вопроса"):
            assert faq_page.is_eighth_question_expanded(), "Текст восьмого вопроса не раскрылся после клика"

        with allure.step("Проверка содержимого ответа"):
            answer_text = faq_page.get_answer_8_text()
            expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
            assert expected_text in answer_text, f"Ожидаемый текст не найден в ответе. Найдено: {answer_text}"
