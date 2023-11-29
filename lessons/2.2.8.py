from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputs = browser.find_elements(By.CLASS_NAME, 'form-control')

    for input in inputs:
        input.send_keys('1')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'application.txt')  # добавляем к этому пути имя файла

    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()