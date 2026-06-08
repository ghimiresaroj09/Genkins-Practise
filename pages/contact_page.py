from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
        self.name_locator = (By.XPATH, "//input[@name='name']")
        self.email_locator = (By.XPATH, "//input[@name='email']")
        self.message_locator = (By.XPATH, "//textarea[@name='message']")
        self.submit_button_locator = (By.XPATH, "//button[@id='contact-submit']")

    def navigate_to_contact_page(self):
        self.click_element(self.contact_link_locator)

    def submit_contact_form(self, name, email, message):
        self.enter_text(self.name_locator, name)
        self.enter_text(self.email_locator, email)
        self.enter_text(self.message_locator, message)
        self.click_element(self.submit_button_locator)
    