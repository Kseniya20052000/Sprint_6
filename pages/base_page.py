import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from urllib.parse import urlparse

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Навигация ---

    @allure.step("Открытие URL")
    def open_url(self, url):
        self.driver.get(url)
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    # --- Поиск элементов ---

    @allure.step("Поиск кликабельного элемента")
    def find_clickable(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Поиск видимого элемента")
    def find_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск присутствующего элемента")
    def find_present(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_invisible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.invisibility_of_element_located(locator))

    # --- Действия с элементами ---

    @allure.step("Клик по элементу")
    def click(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_clickable(element_or_locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик по элементу через JavaScript")
    def click_js(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_visible(element_or_locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в поле")
    def type_text(self, locator, text):
        element = self.find_present(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверка отображения элемента")
    def is_displayed(self, locator, timeout=None):
        try:
            return self.find_visible(locator, timeout).is_displayed()
        except Exception:
            return False

    @allure.step("Получение текста элемента")
    def get_text(self, locator, timeout=None):
        element = self.find_visible(locator, timeout)
        return element.text

    @allure.step("Получение атрибута элемента")
    def get_attribute(self, element_or_locator, attribute, timeout=None):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_visible(element_or_locator, timeout)
        return element.get_attribute(attribute)

    # --- Скролл ---

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_visible(element_or_locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )

    # --- Окна ---

    @allure.step("Получение дескриптора текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получение всех дескрипторов окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключение на окно")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Ожидание нового окна")
    def wait_for_new_window(self, original_count, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > original_count
        )

    @allure.step("Ожидание URL с подстрокой")
    def wait_for_url_contains(self, substring, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )

    @allure.step("Закрытие текущего окна")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Клик по элементу (нативный)")
    def click_native(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_clickable(element_or_locator)
        element.click()



    # Проверка, содержит ли текущий URL подстроку
    def is_current_url_contains(self, substring: str, timeout: int = 10) -> bool:
        return self.wait_for_url_contains(substring, timeout=timeout)

    # Закрытие текущего окна
    def close_current_window(self):
        self.driver.close()  

    # Переключение на окно по хендлу
    def switch_to_window(self, handle: str):
        self.driver.switch_to.window(handle)


    def is_current_url_on_dzen_domain(self, timeout: int = 15) -> bool:
        """Проверяет, что текущий URL относится к домену dzen.ru (включая поддомены)"""
        def condition(driver):
            url = driver.current_url
            parsed = urlparse(url)
            return parsed.netloc.endswith("dzen.ru")

        try:
            WebDriverWait(self.driver, timeout).until(condition)
            return True
        except TimeoutException:
            return False