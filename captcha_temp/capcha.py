from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_capcha():
    driver = webdriver.Firefox()
    driver.get('https://www.prepostseo.com/ru/image-to-text')
    file_input = os.path.abspath('captcha_temp/result.png')
    # file_input = os.path.abspath('captcha_temp/image.png')

    wait = WebDriverWait(driver, 10)
    captcha_send = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    captcha_send.send_keys(file_input)
    time.sleep(2)


    extrude_text_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[4]/div[3]/div[1]')
    extrude_text_button.click()
    time.sleep(10)

    captcha_code = driver.find_element(By.XPATH, '//*[@id="result__text0"]').text
    return captcha_code