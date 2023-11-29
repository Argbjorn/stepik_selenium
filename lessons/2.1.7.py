from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_text = chest.get_attribute('valuex')
    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    input.send_keys(calc(x_text))

    robot_chekbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot_chekbox.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()