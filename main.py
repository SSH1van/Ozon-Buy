from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def is_button_clicked_with_refresh(temp_button):
    try:
        WebDriverWait(driver, 1).until(EC.invisibility_of_element(temp_button))
        return True
    except:
        return False

def is_button_clicked_without_refresh(temp_button):
    try:
        div_element = temp_button.find_element(By.TAG_NAME, "div")       
        div_class = div_element.get_attribute("class")    
        if "active" in div_class:
            return True 
        else:
            return False 
    except Exception:
        return False


driver_path = './chromedriver-win64/chromedriver.exe'
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-webrtc")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(service=service, options=options)

try:
    url = 'https://www.ozon.ru/product/apple-macbook-air-13-2020-noutbuk-13-3-apple-m1-8c-cpu-7c-gpu-ram-8-gb-ssd-256-gb-apple-m1-1628553909/?from=share_ios&utm_campaign=productpage_link&utm_medium=share_button&utm_source=smm'
    driver.get(url)
    
    # Время для входа в личный кабинет
    time.sleep(60)
    
finally:
    time.sleep(120)
    driver.quit()