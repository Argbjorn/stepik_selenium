from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.set_window_size(1920,900)

    browser.get("https://petrovich.ru/catalog/133600757/506118/")
    time.sleep(5)
    add_button = browser.find_element(By.CSS_SELECTOR, '.add-to-cart-button')
    add_button.click()

finally:
    time.sleep(3)
    browser.quit()