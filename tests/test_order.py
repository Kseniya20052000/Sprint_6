import allure
import pytest

@allure.feature("Оформление заказа")
class TestOrderFlow:

    @allure.story("Оформление заказа через кнопку в шапке сайта")
    @allure.title("Заказ через шапку: {name} {surname}")
    @pytest.mark.parametrize(
        "name, surname, address, metro_station, color, comment",
        [
            ("Анна", "Сидорова", "ул. Пушкина, 15", "Преображенская площадь", "black", "Позвонить за час"),
        ],
    )
    def test_complete_order_from_header(self, main_page, name, surname, address, metro_station, color, comment):
        with allure.step("Нажатие на кнопку «Заказать» в шапке"):
            main_page.click_order_button_header()

        self._run_common_order_flow(main_page, name, surname, address, metro_station, color, comment)


    @allure.story("Оформление заказа через кнопку в футере сайта")
    @allure.title("Заказ через футер: {name} {surname}")
    @pytest.mark.parametrize(
        "name, surname, address, metro_station, color, comment",
        [
            ("Иван", "Петров", "ул. Ленина, 1", "Сокольники", "grey", "Не звонить"),
        ],
    )
    def test_complete_order_from_footer(self, main_page, name, surname, address, metro_station, color, comment):
        with allure.step("Нажатие на кнопку «Заказать» в футере"):
            main_page.click_order_button_footer()

        self._run_common_order_flow(main_page, name, surname, address, metro_station, color, comment)


    # Вспомогательный метод для общей логики 
    @staticmethod
    def _run_common_order_flow(page, name, surname, address, metro_station, color, comment):
        with allure.step("Проверка отображения формы заказа"):
            assert page.is_order_form_visible(), "Форма заказа не отображается"

        with allure.step("Заполнение первой формы заказа"):
            page.fill_order_form(
                name=name,
                surname=surname,
                address=address,
                metro_station=metro_station
            )

        with allure.step("Нажатие на кнопку «Далее»"):
            page.click_next_step_button()

        with allure.step("Заполнение второй формы заказа"):
            page.fill_second_order_form(color=color, comment=comment)

        with allure.step("Нажатие на кнопку «Заказать» во второй форме"):
            page.click_submit_order_button()

        with allure.step("Подтверждение заказа в модальном окне"):
            page.confirm_order_in_modal()

        with allure.step("Проверка успешного оформления заказа"):
            assert page.is_order_success_modal_visible(), \
                "Модальное окно с успешным заказом не появилось"

        with allure.step("Получение номера заказа"):
            order_number = page.get_order_number()
            assert order_number is not None, "Не удалось получить номер заказа"
            allure.attach(order_number, "Номер заказа", allure.attachment_type.TEXT)

        with allure.step("Нажатие на кнопку «Посмотреть статус»"):
            page.click_status_button()
