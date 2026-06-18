from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from ..locators.cookie_locators import Cookie
from ..locators.order_locators import Order
import allure


class Orders(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.top_order_button = Order.TOP_ORDER_BUTTON
        self.bottom_order_button = Order.BOTTOM_ORDER_BUTTON
        self.cookie_button = Cookie.COOKIE
        self.name_input = Order.NAME_INPUT
        self.surname_input = Order.SURNAME_INPUT
        self.address_input = Order.ADDRESS_INPUT
        self.metro_input = Order.METRO_INPUT
        self.telephon_input = Order.TELEPHON_INPUT
        self.next_button = Order.NEXT_BUTTON
        self.dropdown_metro = Order.DROPDOWN_METRO
        self.delivery_date = Order.DELIVERY_DATE
        self.rental_period = Order.RENTAL_PERIOD
        self.comment_input = Order.COMMENT_INPUT
        self.forma_order_button = Order.FORMA_ORDER_BUTTON
        self.yes_button = Order.YES_BUTTON
        self.order_decorated_locator = Order.ORDER_DECORATED
        self.status_button = Order.STATUS_BUTTON
        self.scooter_logo = Order.SCOOTER_LOGO
        self.yandex_logo = Order.YANDEX_LOGO
        self.body = Order.BODY

    @allure.step("Принять куки")
    def click_cookie(self):
        self.click(self.cookie_button)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_top(self):
        self.click(self.top_order_button)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_bottom(self):
        self.click(self.bottom_order_button)

    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.send_keys(self.name_input, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_surname(self, surname):
        self.send_keys(self.surname_input, surname)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.send_keys(self.address_input, address)

    @allure.step("Заполнить поле 'Станция метро'")
    def set_metro(self, metro):
        self.click(self.metro_input)
        self.send_keys(self.metro_input, metro)
        self.wait.until(EC.presence_of_element_located(self.dropdown_metro))
        self.click(self.dropdown_metro)

    @allure.step("Заполнить поле 'Телефон'")
    def set_telephon(self, telephon):
        self.send_keys(self.telephon_input, telephon)

    @allure.step("Нажать на кнопку 'Далее'")
    def click_next(self):
        self.click(self.next_button)

    def forma_order1(self, name, surname, address, metro, telephon):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_telephon(telephon)
        self.click_next()
        self.wait.until(EC.presence_of_element_located(self.delivery_date))

    @allure.step("Заполнить поле 'Когда привезти самокат'")
    def set_delivery(self, delivery):
        self.send_keys(self.delivery_date, delivery)
        self.wait.until(EC.text_to_be_present_in_element_value(self.delivery_date, delivery))
        self.click(self.body)

    @allure.step("Заполнить поле 'Срок аренды'")
    def set_period(self, period):
        self.click(self.rental_period)
        self.wait.until(EC.presence_of_element_located(period))
        self.click(period)

    @allure.step("Заполнить поле 'Комментарий'")
    def set_comment(self, comment):
        self.send_keys(self.comment_input, comment)

    @allure.step("Заполнить поле 'Цвет самоката'")
    def set_color(self, color):
        self.click(color)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_forma(self):
        self.click(self.forma_order_button)

    def forma_order2(self, delivery, period, color, comment):
        self.set_delivery(delivery)
        self.set_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_forma()

    @allure.step("Нажать кнопку 'Да'")
    def click_yes(self):
        self.click(self.yes_button)

    def order_decorated(self):
        return self.is_displayed(self.order_decorated_locator)

    @allure.step("Нажать кнопку 'Посмотреть статус'")
    def click_status(self):
        self.click(self.status_button)

    @allure.step("Нажать логотип Самокат")
    def click_scooter(self):
        self.click(self.scooter_logo)

    @allure.step("Нажать логотип Яндекс")
    def click_yandex(self):
        self.click(self.yandex_logo)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать открытия новой вкладки")
    def wait_for_new_tab(self, expected_number_of_windows=2):
        self.wait.until(EC.number_of_windows_to_be(expected_number_of_windows))

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Переключиться на вкладку по индексу")
    def switch_to_tab_by_index(self, index=-1):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step("Кликнуть на логотип Яндекс и переключиться на новую вкладку")
    def click_yandex_and_switch_to_new_tab(self):
        initial_tabs = len(self.driver.window_handles)
        self.click_yandex()
        self.wait.until(lambda driver: len(driver.window_handles) > initial_tabs)
        self.wait_for_new_tab()
        self.switch_to_new_tab()
        self.wait_for_page_load()
        self.wait.until(lambda driver: driver.current_url != "about:blank")