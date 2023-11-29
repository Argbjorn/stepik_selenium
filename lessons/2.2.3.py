from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    answer = int(browser.find_element(By.CSS_SELECTOR, '#num1').text) + int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    print(answer)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(answer))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()