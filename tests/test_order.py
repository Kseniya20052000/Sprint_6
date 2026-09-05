import allure
import pytest


@allure.feature("Оформление заказа")
@allure.story("Полное оформление заказа через разные точки входа с разными данными")
class TestOrderFlow:

    @pytest.mark.parametrize(
        "entry_point, name, surname, address, metro_station, color, comment",
        [
            ("header", "Анна", "Сидорова", "ул. Пушкина, 15", "Преображенская площадь", "black", "Позвонить за час"),
            ("footer", "Иван", "Петров", "ул. Ленина, 1", "Сокольники", "grey", "Не звонить"),
        ],
    )
    @allure.title("Заказ через кнопку {entry_point}: {name} {surname}")
    def test_complete_order_flow(self, main_page, entry_point, name, surname, address, metro_station, color, comment):
        with allure.step(f"Нажатие на кнопку «Заказать» ({entry_point})"):
            if entry_point == "header":
                main_page.click_order_button_header()
            else:
                main_page.click_order_button_footer()

        with allure.step("Проверка отображения формы заказа"):
            assert main_page.is_order_form_visible(), "Форма заказа не отображается"

        with allure.step("Заполнение первой формы заказа"):
            main_page.fill_order_form(
                name=name,
                surname=surname,
                address=address,
                metro_station=metro_station
            )

        with allure.step("Нажатие на кнопку «Далее»"):
            main_page.click_next_step_button()

        with allure.step("Заполнение второй формы заказа"):
            main_page.fill_second_order_form(color=color, comment=comment)

        with allure.step("Нажатие на кнопку «Заказать» во второй форме"):
            main_page.click_submit_order_button()

        with allure.step("Подтверждение заказа в модальном окне"):
            main_page.confirm_order_in_modal()

        with allure.step("Проверка успешного оформления заказа"):
            assert main_page.is_order_success_modal_visible(), \
                "Модальное окно с успешным заказом не появилось"

        with allure.step("Получение номера заказа"):
            order_number = main_page.get_order_number()
            assert order_number is not None, "Не удалось получить номер заказа"
            allure.attach(order_number, "Номер заказа", allure.attachment_type.TEXT)

        with allure.step("Нажатие на кнопку «Посмотреть статус»"):
            main_page.click_status_button()
