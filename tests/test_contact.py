import pytest
import allure
from selenium.webdriver.common.by import By

from pages.contact_page import ContactPage
from utilities.browser_utils import BrowserUtils


@allure.feature("Contact Form")
@allure.story("Submit Contact Form")
@allure.title("Test Contact Form Submission with Valid Data")
@allure.severity(allure.severity_level.MINOR)
def test_contact_form_submission(driver):

    contact_page = ContactPage(driver)
    browser_utils = BrowserUtils(driver)

    with allure.step('Open website'):
        contact_page.open_page()

    with allure.step("Navigate to contact page"):
        contact_page.navigate_to_contact_page()

    with allure.step("Submit contact form with valid data"):
        contact_page.submit_contact_form(
            "John Doe",
            "john.doe@example.com",
            "This is a test message."
        )

    with allure.step("Verify success message is displayed"):
        success_message = contact_page.get_element_text((By.XPATH, "//p[@class = 'mt-4']"))
        assert success_message == "The form was submitted successfully."