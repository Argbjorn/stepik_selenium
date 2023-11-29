from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

