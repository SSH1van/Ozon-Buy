from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time

chrome_options = Options()
chrome_options.add_argument("user-data-dir=D:/Work/Programming/Ozon-Buy/Data/User Data Kudrik")
chrome_options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.ozon.ru/cart")

try:
    # Время для входа в личный кабинет
    time.sleep(5)

    while True:
        price_element = driver.find_element(By.CLASS_NAME, "c3022-a1")
        price_text = price_element.text
        price = int(''.join(filter(str.isdigit, price_text)))
        if price < 62000:
            break

        driver.refresh()
        time.sleep(random.uniform(0.5, 2))
        driver.execute_script("window.stop();")
    
    button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b2120-a0') and .//div[text()='Перейти к оформлению']]"))
        )
    button.click()
    button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b2120-a0') and .//div[text()='Оплатить онлайн']]"))
        )
    button.click()   
finally:
    time.sleep(120)
    driver.quit()