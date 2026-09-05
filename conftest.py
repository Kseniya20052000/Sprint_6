import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.faq_page import FAQPage
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


@pytest.fixture
def faq_page(driver, base_url):
    driver.get(base_url)
    return FAQPage(driver)


@pytest.fixture
def main_page(driver, base_url):
    page = MainPage(driver)
    page.open(base_url)
    return page


@pytest.fixture(scope="session")
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"
