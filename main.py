from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time
import os

def start(user_data, price_max, time_wait, headless):
    relative_path = os.path.join("Data", user_data)
    absolute_path = os.path.abspath(relative_path)

    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    chrome_options.add_argument(f"user-data-dir={absolute_path}")
    chrome_options.add_argument("profile-directory=Default")
    if headless:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ozon.ru/cart")

    try:
        time.sleep(time_wait)

        while True:
            try:
                price_element = driver.find_element(By.XPATH, '//span[@class="c3022-a1 tsHeadline400Small c3022-b1 c3022-a5"]')
                price_text = price_element.text
                price = int(''.join(filter(str.isdigit, price_text)))
                if price < price_max:
                    # print(price)
                    break

                driver.refresh()
                time.sleep(random.uniform(0.5, 2))
                driver.execute_script("window.stop();")
            except:
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
        print("bought")   
    finally:
        time.sleep(120)
        driver.quit()