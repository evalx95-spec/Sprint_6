from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверить видимость элемента")
    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть с прокруткой")
    def click_with_scroll(self, locator):
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Нажать на элемент и дождаться появления другого")
    def click_and_wait_for_element(self, click_locator, wait_locator):
        self.click_with_scroll(click_locator)
        self.wait.until(EC.visibility_of_element_located(wait_locator))

    @allure.step("Нажать на кнопку 'Принять куки'")
    def click_cookie(self, cookie_locator):
        self.click(cookie_locator)

    @allure.step("Ожидать исчезновения элемента")
    def wait_until_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидать, что элемент станет кликабельным и кликнуть")
    def click_when_ready(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()