from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(driver):

    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title('Samsung galaxy s6')


def test_click(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_prod_count(2)