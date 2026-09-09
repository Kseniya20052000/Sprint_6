import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.faq_page import FAQPage
from pages.main_page import MainPage
from dotenv import load_dotenv
import os


# Загружаем переменные из .env при старте pytest
load_dotenv()

@pytest.fixture(scope="function")
def driver():
    
    driver_path = os.path.join(os.getcwd(), "geckodriver.exe")

    service = FirefoxService(executable_path=driver_path)
    browser = webdriver.Firefox(service=service)
    yield browser
    browser.quit()


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
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("Переменная BASE_URL не найдена в .env или переменных окружения")
    return url
