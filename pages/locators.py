from selenium.webdriver.common.by import By

class FAQPageLocators:
    # Общие локаторы
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")  # для раздела FAQ

    # Локаторы для вопросов
    QUESTION_1_BUTTON = (By.ID, "accordion__heading-0")
    QUESTION_2_BUTTON = (By.ID, "accordion__heading-1")
    QUESTION_3_BUTTON = (By.ID, "accordion__heading-2")
    QUESTION_4_BUTTON = (By.ID, "accordion__heading-3")
    QUESTION_5_BUTTON = (By.ID, "accordion__heading-4")
    QUESTION_6_BUTTON = (By.ID, "accordion__heading-5")
    QUESTION_7_BUTTON = (By.ID, "accordion__heading-6")
    QUESTION_8_BUTTON = (By.ID, "accordion__heading-7")

    # Локаторы для ответов
    ANSWER_1_TEXT = (By.ID, "accordion__panel-0")
    ANSWER_2_TEXT = (By.ID, "accordion__panel-1")
    ANSWER_3_TEXT = (By.ID, "accordion__panel-2")
    ANSWER_4_TEXT = (By.ID, "accordion__panel-3")
    ANSWER_5_TEXT = (By.ID, "accordion__panel-4")
    ANSWER_6_TEXT = (By.ID, "accordion__panel-5")
    ANSWER_7_TEXT = (By.ID, "accordion__panel-6")
    ANSWER_8_TEXT = (By.ID, "accordion__panel-7")

class MainPageLocators:
    # Локатор для кнопки «Заказать» в шапке сайта (используем класс как наиболее стабильный селектор)
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, "button.Button_Button__ra12g")

    # Локатор для формы заказа на странице заказа
    ORDER_FORM = (By.CLASS_NAME, "Order_Form__17u6u")

    # Локаторы для полей формы заказа (для дополнительной верификации)
    ORDER_INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    ORDER_INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ORDER_INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    ORDER_INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Локатор для кнопки «Заказать» в нижней части сайта
    ORDER_BUTTON_FOOTER = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")


    # Локатор для поля «Станция метро»
    METRO_STATION_INPUT = (By.XPATH, "//div[@class='select-search__value']//input[@placeholder='* Станция метро']")

    # Локатор для кнопки «Далее»
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")

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

    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")

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

    PROMO_WINDOW_YES_BTN = (By.XPATH, "//a[normalize-space()='Да']")
    SEARCH_BAR = (By.CSS_SELECTOR, ".dzen-search-arrow-common__arrow")