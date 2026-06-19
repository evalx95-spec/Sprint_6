import pytest
from selenium import webdriver
from .urls import Urls


@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.HOME_PAGE)
    driver.implicitly_wait(5) 
    yield driver
    driver.quit()