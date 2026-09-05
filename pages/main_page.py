from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from .locators import MainPageLocators
import random
from selenium.common.exceptions import TimeoutException

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Открывает страницу по указанному URL"""
        self.driver.get(url)
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def close_cookie_banner(self):
        """Закрывает баннер куки, если он есть"""
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
        except Exception:
            pass

    # --- Точки входа ---

    def click_order_button_header(self):
        """Кликает на кнопку «Заказать» в шапке сайта"""
        button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        )
        button.click()

    def click_order_button_footer(self):
        """Кликает на кнопку «Заказать» внизу страницы"""
        self.close_cookie_banner()

        button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_FOOTER)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )

        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", button)

    # --- Первая форма ---

    def is_order_form_visible(self):
        """Проверяет, что форма заказа отображается на странице"""
        try:
            form = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_FORM)
            )
            return form.is_displayed()
        except Exception:
            return False

    def get_order_form_elements(self):
        """Получает все элементы формы заказа для дополнительной верификации"""
        elements = {}
        try:
            elements['name_input'] = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_NAME)
            )
            elements['surname_input'] = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_SURNAME)
            )
            elements['address_input'] = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_ADDRESS)
            )
            elements['phone_input'] = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_PHONE)
            )
        except Exception:
            pass
        return elements

    def fill_order_form(self, name="Иван", surname="Петров", address="ул. Ленина, 1",
                        metro_station="Преображенская площадь"):
        """Заполняет первую форму заказа"""
        self.close_cookie_banner()

        name_input = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_NAME)
        )
        name_input.clear()
        name_input.send_keys(name)

        surname_input = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_SURNAME)
        )
        surname_input.clear()
        surname_input.send_keys(surname)

        address_input = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_ADDRESS)
        )
        address_input.clear()
        address_input.send_keys(address)

        # --- Выбор станции метро ---
        metro_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.select-search__input"))
        )
        metro_input.click()

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.select-search__select"))
        )

        option_locator = (
            By.XPATH,
            f"//div[contains(@class, 'select-search__select')]//*[normalize-space()='{metro_station}']"
        )
        option_element = self.wait.until(EC.element_to_be_clickable(option_locator))
        option_element.click()

        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.select-search__select"))
        )

        # --- Телефон ---
        phone = self._generate_random_phone()
        phone_input = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_INPUT_PHONE)
        )
        phone_input.clear()
        phone_input.send_keys(phone)

    def _generate_random_phone(self):
        """Генерирует случайный номер телефона в формате +7XXXXXXXXXX"""
        return f"+7{random.randint(1000000000, 9999999999)}"

    def click_next_step_button(self):
        """Кликает на кнопку «Далее» на первой форме"""
        next_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.NEXT_BUTTON)
        )
        next_button.click()

    # --- Вторая форма ---

    def fill_second_order_form(self, color="black", comment=":)"):
        """Заполняет вторую форму заказа"""
        # 1. Выбираем дату 
        
        date_input = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.DATE_INPUT)
        )
        date_input.click()

        today_day = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.DATE_PICKER_TODAY)
        )
        today_day.click()
        

        # 2. Выбираем срок аренды (сутки)
        rent_dropdown = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.RENT_PERIOD_DROPDOWN)
        )
        rent_dropdown.click()

        rent_option = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.RENT_PERIOD_OPTION)
        )
        rent_option.click()

        # 3. Выбираем цвет самоката
        if color == "black":
            color_checkbox = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COLOR_BLACK_CHECKBOX)
            )
        else:
            color_checkbox = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COLOR_GREY_CHECKBOX)
            )
        color_checkbox.click()

        # 4. Вводим комментарий
        comment_input = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.COMMENT_INPUT)
        )
        comment_input.clear()
        comment_input.send_keys(comment)

    def click_submit_order_button(self):
        """Кликает на кнопку «Заказать» на второй форме"""
        btn_locator = (
            By.XPATH,
            "//div[contains(@class, 'Order_Buttons')]//button[normalize-space()='Заказать']"
        )
        btn = self.wait.until(EC.element_to_be_clickable(btn_locator))

        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

    # --- Модальное окно подтверждения ---

    def confirm_order_in_modal(self):
        """Подтверждает заказ в модальном окне (нажимает «Да»)"""
        yes_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CONFIRM_YES)
        )
        yes_button.click()

    def is_order_success_modal_visible(self):
        """Проверяет, что модальное окно с успешным оформлением заказа отображается"""
        try:
            modal = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_SUCCESS_MODAL)
            )
            return modal.is_displayed()
        except Exception:
            return False

    def get_order_number(self):
        """Получает номер заказа из модального окна"""
        try:
            order_number_element = self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER)
            )
            return order_number_element.text
        except Exception:
            return None

    def click_status_button(self):
        """Кликает на кнопку «Посмотреть статус»"""
        status_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.STATUS_BUTTON)
        )
        status_button.click()

    # --- Навигация ---

    def click_logo(self):
        """Кликает на логотип «Самокат»"""
        logo_link = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGO_LINK)
        )
        logo_link.click()

    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url


    #Яндекс.дзен
    def click_yandex_logo_and_switch_to_new_window(self):
        """Клик по логотипу Яндекса и переключение на новое окно"""
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        original_handle = self.driver.current_window_handle
        original_count = len(self.driver.window_handles)

        logo.click()

        # Ждём появления нового окна
        WebDriverWait(self.driver, 15).until(
            lambda d: len(d.window_handles) > original_count
        )

        # Ищем новый хендл
        new_handle = next(
            h for h in self.driver.window_handles if h != original_handle
        )
        self.driver.switch_to.window(new_handle)
        return original_handle  # Возвращаем исходный хендл для возврата

        # Новый метод: "Если есть окно с кнопкой 'Да' — закрой его"
    
    def close_promo_window_if_present(self):
        """
        Пытается найти и нажать кнопку 'Да' в промо-окне.
        Если окна нет — просто ничего не делает и не падает.
        """
        btn_locator = MainPageLocators.PROMO_WINDOW_YES_BTN
        
        try:
            # 1. Ждём, пока станет кликабельной
            btn_yes = self.wait.until(EC.element_to_be_clickable(btn_locator))
            
            # 2. Клик через JS (чтобы обойти перекрытие анимацией)
            self.driver.execute_script("arguments[0].click();", btn_yes)
            
            # 3. Ждём, пока кнопка реально исчезнет из DOM
            self.wait.until(EC.invisibility_of_element_located(btn_locator))
            print("Промо-окно закрыто") # Для отладки в консоли
            
        except TimeoutException:
            # Кнопки нет — это нормально, продолжаем работу
            pass