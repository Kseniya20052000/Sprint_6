from selenium.webdriver.common.by import By

class FAQPageLocators:
    # Общие локаторы
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")

    # Универсальные локаторы — индекс подставляется через .format()
    QUESTION_BUTTON = (By.ID, "accordion__heading-{}")
    ANSWER_PANEL = (By.ID, "accordion__panel-{}")

class MainPageLocators:
    # Локатор для кнопки «Заказать» в шапке сайта 
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[normalize-space()='Заказать']")

    # Локатор для формы заказа на странице заказа
    ORDER_FORM = (By.CLASS_NAME, "Order_Form__17u6u")

    # Локаторы для полей формы заказа (для дополнительной верификации)
    ORDER_INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    ORDER_INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ORDER_INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    ORDER_INPUT_PHONE = (By.XPATH, "//input[@type='text' and following-sibling::div[contains(text(), 'Введите корректный номер')]]")

    # Локатор для кнопки «Заказать» в нижней части сайта
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[normalize-space()='Заказать']")


    # Локатор для поля «Станция метро»
    METRO_STATION_INPUT = (By.XPATH, "//div[@class='select-search__value']//input[@placeholder='* Станция метро']")

    # Локатор для кнопки «Далее»
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[normalize-space()='Далее']")

    # Локатор для элемента в списке станций метро (конкретная станция)
    METRO_STATION_OPTION = (By.XPATH, "//li[contains(text(), 'Преображенская площадь')]")


    # Локаторы для второй формы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_TODAY = (By.CSS_SELECTOR, "div.react-datepicker__day--today")

    RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "div.Dropdown-control")
    RENT_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    COLOR_BLACK_CHECKBOX = (By.ID, "black")  # чёрный жемчуг
    COLOR_GREY_CHECKBOX = (By.ID, "grey")  # серая безысходность

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[normalize-space()='Заказать']")

    # Локаторы для модального окна подтверждения
    MODAL_CONFIRM_NO = (By.XPATH, "//button[contains(text(), 'Нет')]")
    MODAL_CONFIRM_YES = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(@class, 'Order_Buttons')]//button[normalize-space()='Да']")

    # Локатор для успешного оформления заказа
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(text(), 'Номер заказа:')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")

    #для кнопки "Самокат"
    LOGO_LINK = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    # Локаторы для теста с Яндексом и Дзеном
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    DZHEN_LOGO = (By.XPATH, "//svg[contains(@class, 'dzen-layout--desktop-base-header__logoWithText-3k')]")

    DZEN_CLOSE_BTN = (By.XPATH, "//span[@aria-label='Закрыть']")
    SEARCH_BAR = (By.CSS_SELECTOR, ".dzen-search-arrow-common__arrow")