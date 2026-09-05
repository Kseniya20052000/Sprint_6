import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.main_page import MainPage
from pages.locators import MainPageLocators


@allure.feature("Навигация по внешним ссылкам")
@allure.story("Проверка перехода на Дзен через логотип Яндекса")
def test_yandex_logo_redirect(driver, base_url):
    main_page = MainPage(driver)
    main_page.open(base_url)

    with allure.step("Клик по логотипу Яндекса и переход в новое окно"):
        original_handle = main_page.click_yandex_logo_and_switch_to_new_window()
        wait = WebDriverWait(driver, 15)

    try:
        
        with allure.step("Закрытие всплывающего окна (если есть)"):
            main_page.close_promo_window_if_present()

        with allure.step("Проверка перехода на Дзен"):
            WebDriverWait(driver, 20).until(
                lambda d: "dzen.ru" in d.current_url
            )

        with allure.step("Проверка строки поиска"):
            # Используем локатор из файла, но ожидание делаем здесь или через метод страницы
            search_bar = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(MainPageLocators.SEARCH_BAR)
            )
            assert search_bar.is_displayed()
            
    finally:
        with allure.step("Возврат в исходное окно"):
            driver.close()
            driver.switch_to.window(original_handle)