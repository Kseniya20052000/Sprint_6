import allure
from pages.main_page import MainPage


@allure.feature("Навигация по внешним ссылкам")
@allure.story("Проверка перехода на Дзен через логотип Яндекса")
@allure.title("Переход на Дзен: клик по логотипу и проверка URL")
def test_yandex_logo_redirect(driver, base_url):
    main_page = MainPage(driver)
    main_page.open(base_url)

    with allure.step("Клик по логотипу Яндекса и переключение на Дзен"):
        original_handle = main_page.go_to_dzen()

    with allure.step("Проверка, что перешли на домен dzen.ru"):
        assert main_page.is_current_url_on_dzen_domain(), \
            f"Ожидался домен dzen.ru, получили {main_page.get_current_url()}"

    with allure.step("Возврат в исходное окно"):
        main_page.close_current_window()
        main_page.switch_to_window(original_handle)
