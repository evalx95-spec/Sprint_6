import allure
import pytest
from ..user_data import UserData
from ..pages.order_page import Orders

@allure.feature("Заказы")
class TestOrder:
    @allure.title("Проверка верхней кнопки Заказать")
    @pytest.mark.parametrize("user_data", [UserData.USER1])
    def test_order_top(self, driver, user_data):
        order1 = Orders(driver)
        order1.click_cookie()
        order1.click_order_top()

        order1.forma_order1(**user_data["order1"])
        order1.forma_order2(**user_data["order2"])

        order1.click_yes()

        assert order1.order_decorated()

    @allure.title("Проверка нижней кнопки Заказать")
    @pytest.mark.parametrize("user_data", [UserData.USER2])
    def test_order_bottom(self, driver, user_data):
        order2 = Orders(driver)
        order2.click_cookie()
        order2.click_order_bottom()

        order2.forma_order1(**user_data["order1"])
        order2.forma_order2(**user_data["order2"])

        order2.click_yes()
        assert order2.order_decorated()

    @allure.title("Переход на главную страницу при клике на логотип 'Самокат'")
    def test_scooter_logo_redirect(self, driver):
        order = Orders(driver)
        order.click_cookie()
        order.click_scooter()
        assert order.get_current_url() == "https://qa-scooter.education-services.ru/" 


    @allure.title("Переход на страницу Яндекса при клике на логотип 'Яндекс'")
    def test_yandex_logo_redirect(self, driver):
        order = Orders(driver)
        order.click_cookie()
        order.click_yandex_and_switch_to_new_tab()
        assert "https://ya.ru/" in order.get_current_url()