import allure
from pages.main_page import MainPage


@allure.feature("Навигация по внешним ссылкам")
@allure.story("Проверка перехода на Дзен через логотип Яндекса")
def test_yandex_logo_redirect(driver, base_url):
    main_page = MainPage(driver)
    main_page.open(base_url)

    with allure.step("Клик по логотипу и переключение на Дзен"):
        original_handle = main_page.go_to_dzen()

    # если модалка есть — закроется, если нет — метод внутри страницы ничего не сделает
    with allure.step("Закрытие всплывающего окна на Дзене (если есть)"):
        main_page.close_dzen_popup(timeout=15)

    with allure.step("Проверка URL на Дзене"):
        assert "dzen.ru" in driver.current_url, f"Ожидался dzen.ru, получили {driver.current_url}"

    with allure.step("Проверка строки поиска на Дзене"):
        assert main_page.is_search_bar_visible(), "Строка поиска не найдена"

    with allure.step("Возврат в исходное окно"):
        driver.close()
        driver.switch_to.window(original_handle)
