import allure
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Навигация по сайту")
@allure.story("Проверка перехода на главную страницу через логотип «Самокат»")
def test_logo_navigation(main_page, base_url):
    """
    Тест: нажимаем на логотип «Самокат» → попадаем на главную страницу.
    Сценарий:
    1. Открываем главную страницу.
    2. Нажимаем «Заказать» → появляется форма заказа.
    3. Нажимаем на логотип «Самокат» → переходим на главную.
    4. Проверяем, что URL совпадает с base_url.
    """
    with allure.step("Открытие главной страницы сайта"):        
        assert main_page.get_current_url() == base_url, \
            f"Ожидался URL: {base_url}, но получен: {main_page.get_current_url()}"

    with allure.step("Нажатие на кнопку «Заказать» в шапке сайта"):
        main_page.click_order_button_header()

    with allure.step("Нажатие на логотип «Самокат»"):
        main_page.click_logo()

    with allure.step("Проверка, что мы вернулись на главную страницу"):
        WebDriverWait(main_page.driver, 15).until(
            lambda d: d.current_url == base_url
        )
        assert main_page.get_current_url() == base_url, \
            f"Ожидался URL: {base_url}, но получен: {main_page.get_current_url()}"
