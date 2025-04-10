from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def is_inventory_page_displayed(self):
        return self.wait_for_element(self.INVENTORY_CONTAINER).is_displayed()

    def add_product_to_cart(self, product_name):
        product_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(product_locator)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)
