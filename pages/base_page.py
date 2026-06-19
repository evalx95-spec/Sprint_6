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

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Переключиться на вкладку по индексу")
    def switch_to_tab_by_index(self, index=-1):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать открытия новой вкладки")
    def wait_for_new_tab(self, expected_number_of_windows=2):
        self.wait.until(EC.number_of_windows_to_be(expected_number_of_windows))

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
