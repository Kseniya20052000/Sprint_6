from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Навигация ---

    def open_url(self, url):
        self.driver.get(url)
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_current_url(self):
        return self.driver.current_url

    # --- Поиск элементов ---

    def find_clickable(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.visibility_of_element_located(locator))

    def find_present(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_element_located(locator))

    def wait_until_invisible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.invisibility_of_element_located(locator))

    # --- Действия с элементами ---

    def click(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_clickable(element_or_locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_js(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_visible(element_or_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.find_present(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator, timeout=None):
        try:
            return self.find_visible(locator, timeout).is_displayed()
        except Exception:
            return False

    def get_text(self, locator, timeout=None):
        element = self.find_visible(locator, timeout)
        return element.text

    def get_attribute(self, element_or_locator, attribute, timeout=None):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_visible(element_or_locator, timeout)
        return element.get_attribute(attribute)

    # --- Скролл ---

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

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def wait_for_new_window(self, original_count, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > original_count
        )

    def wait_for_url_contains(self, substring, timeout=15):
        """Ждёт, пока URL будет содержать указанную подстроку"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )

    def close_current_window(self):
        """Закрывает текущее окно браузера"""
        self.driver.close()

    def click_native(self, element_or_locator):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.find_clickable(element_or_locator)
        element.click()