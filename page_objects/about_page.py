import yaml
from selenium.webdriver.common.by import By

class AboutPage:
    def __init__(self, driver):
        self.driver = driver
        with open('config.yaml') as f:
            self.locators = yaml.safe_load(f)['AboutPage']

    def get_header_font_size(self):
        header_element = self.driver.find_element(By.XPATH, self.locators['header'])
        return header_element.value_of_css_property("font-size")
