import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

service = Service()

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_about_page():
    print("Open link")
    driver = webdriver.Chrome(service=service)
    driver.get(data["address"])

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mdc-text-field__input")))

    username_field = driver.find_element(By.CLASS_NAME, "mdc-text-field__input")
    username_field.send_keys(data["LoginPage"]["login_data"]["username"])

    password_fields = driver.find_elements(By.CLASS_NAME, "mdc-text-field__input")
    if len(password_fields) > 1:
        password_fields[1].send_keys(data["LoginPage"]["login_data"]["password"])

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mdc-button"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About"))).click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='svelte-z9xc0' and text()='About Page']")))
        print("Successfully navigated to the About page.")
    except TimeoutException:
        print("Failed to load the About page.")

    driver.quit()

test_about_page()
