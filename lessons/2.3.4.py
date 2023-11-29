from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()