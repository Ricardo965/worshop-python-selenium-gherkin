from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    CONFIRMATION_MESSAGE = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)
