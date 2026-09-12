import random
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    @allure.step("Открывает страницу по указанному URL и ждёт полной загрузки DOM")
    def open(self, url):
        self.open_url(url)

    @allure.step("Закрывает баннер куки (если присутствует)")
    def close_cookie_banner(self):
        cookie_locator = (By.ID, "rcc-confirm-button")
        try:
            self.click(cookie_locator, timeout=5)
            self.wait_until_invisible(cookie_locator, timeout=5)
        except Exception:
            pass

    # --- Точки входа ---

    @allure.step("Кликает на кнопку «Заказать» в шапке сайта")
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликает на кнопку «Заказать» внизу страницы (с прокруткой и обработкой перекрытия)")
    def click_order_button_footer(self):
        self.close_cookie_banner()
        button = self.find_clickable(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.scroll_to_element(button)
        self.click(button)

    # --- Первая форма ---

    @allure.step("Проверяет, что форма заказа отображается на странице")
    def is_order_form_visible(self):
        return self.is_displayed(MainPageLocators.ORDER_FORM)

    @allure.step("Получает все элементы формы заказа для дополнительной верификации")
    def get_order_form_elements(self):
        elements = {}
        try:
            elements['name_input'] = self.find_present(MainPageLocators.ORDER_INPUT_NAME)
            elements['surname_input'] = self.find_present(MainPageLocators.ORDER_INPUT_SURNAME)
            elements['address_input'] = self.find_present(MainPageLocators.ORDER_INPUT_ADDRESS)
            elements['phone_input'] = self.find_present(MainPageLocators.ORDER_INPUT_PHONE)
        except Exception:
            pass
        return elements

    @allure.step("Заполняет первую форму заказа (имя, фамилия, адрес, метро, телефон)")
    def fill_order_form(self, name="Иван", surname="Петров", address="ул. Ленина, 1",
                        metro_station="Преображенская площадь"):
        self.close_cookie_banner()

        self.type_text(MainPageLocators.ORDER_INPUT_NAME, name)
        self.type_text(MainPageLocators.ORDER_INPUT_SURNAME, surname)
        self.type_text(MainPageLocators.ORDER_INPUT_ADDRESS, address)

        # --- Выбор станции метро ---
        metro_input_locator = (By.CSS_SELECTOR, "input.select-search__input")
        metro_dropdown_locator = (By.CSS_SELECTOR, "div.select-search__select")
        option_locator = (
            By.XPATH,
            f"//div[contains(@class, 'select-search__select')]//*[normalize-space()='{metro_station}']"
        )

        self.click(metro_input_locator)
        self.find_visible(metro_dropdown_locator)
        self.click(option_locator)
        self.wait_until_invisible(metro_dropdown_locator)

        # --- Телефон ---
        phone = self._generate_random_phone()
        self.type_text(MainPageLocators.ORDER_INPUT_PHONE, phone)

    def _generate_random_phone(self):
        return f"+7{random.randint(1000000000, 9999999999)}"

    @allure.step("Нажимает кнопку «Далее» на первой форме заказа")
    def click_next_step_button(self):
        self.click(MainPageLocators.NEXT_BUTTON)

    # --- Вторая форма ---

    @allure.step("Заполняет вторую форму заказа (дата, срок аренды, цвет самоката, комментарий)")
    def fill_second_order_form(self, color="black", comment=":)"):
        # 1. Дата
        self.click(MainPageLocators.DATE_INPUT)
        self.click(MainPageLocators.DATE_PICKER_TODAY)

        # 2. Срок аренды
        self.click(MainPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(MainPageLocators.RENT_PERIOD_OPTION)

        # 3. Цвет самоката
        if color == "black":
            self.click(MainPageLocators.COLOR_BLACK_CHECKBOX)
        else:
            self.click(MainPageLocators.COLOR_GREY_CHECKBOX)

        # 4. Комментарий
        self.type_text(MainPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажимает кнопку «Заказать» на второй форме заказа")
    def click_submit_order_button(self):
        self.click(MainPageLocators.CONFIRM_ORDER_BUTTON)

    # --- Модальное окно подтверждения ---

    @allure.step("Подтверждает заказ в модальном окне (нажимает «Да»)")
    def confirm_order_in_modal(self):
        self.click(MainPageLocators.MODAL_CONFIRM_YES)

    @allure.step("Проверяет, что модальное окно с успешным оформлением заказа отображается")
    def is_order_success_modal_visible(self):
        return self.is_displayed(MainPageLocators.ORDER_SUCCESS_MODAL)

    @allure.step("Получает номер заказа из модального окна")
    def get_order_number(self):
        try:
            return self.get_text(MainPageLocators.ORDER_NUMBER)
        except Exception:
            return None

    @allure.step("Нажимает кнопку «Посмотреть статус»")
    def click_status_button(self):
        self.click(MainPageLocators.STATUS_BUTTON)

    # --- Навигация ---

    @allure.step("Кликает на логотип «Самокат» для перехода на главную")
    def click_logo(self):
        self.click(MainPageLocators.LOGO_LINK)

    @allure.step("Возвращает текущий URL страницы")
    def get_current_url(self):
        return super().get_current_url()

    # Яндекс.Дзен


    @allure.step("Клик по логотипу Яндекса и переключение на Дзен")
    def go_to_dzen(self):
        original = self.driver.current_window_handle
    
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()
    
        import time
        for _ in range(30):
            if len(self.driver.window_handles) > 1:
                break
            time.sleep(1)
    
        for h in self.driver.window_handles:
            if h != original:
                self.driver.switch_to.window(h)
                break
    
        # Ждём, пока URL сменится с about:blank на dzen.ru
        for _ in range(30):
            if "dzen.ru" in self.driver.current_url:
                break
            time.sleep(1)
    
        return original


    @allure.step("Закрывает всплывающее окно на Дзене (крестик)")
    def close_dzen_popup(self, timeout=15):
        """
        Пытается закрыть всплывающее окно на Дзене.
        Если кнопки нет — просто ничего не делает (не выбрасывает ошибку).
        Вся обработка исключений — внутри метода страницы, а не в тесте.
        """
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.DZEN_CLOSE_BTN),
                timeout=timeout
            )
            self.driver.execute_script("arguments[0].click();", btn)
        except Exception:
            # Окно либо не появилось, либо уже закрыто — это не ошибка теста
            pass


    @allure.step("Проверяет, что строка поиска Дзена отображается")
    def is_search_bar_visible(self):
        return self.is_displayed(MainPageLocators.SEARCH_BAR, timeout=15)