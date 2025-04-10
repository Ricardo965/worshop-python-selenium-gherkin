from behave import when, then
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

@when('the user adds "{product_name}" to the cart')
def step_add_product_to_cart(context, product_name):
    if not hasattr(context, "inventory_page"):  # Verifica si ya existe
        context.inventory_page = InventoryPage(context.driver)  # Inicializa solo si no existe
    context.inventory_page.add_product_to_cart(product_name)

@when('proceeds to checkout')
def step_proceed_to_checkout(context):
    if not hasattr(context, "inventory_page"):  # Asegura que esté inicializado
        context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.go_to_cart()
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.proceed_to_checkout()

@when('enters shipping details "{first_name}" "{last_name}" "{postal_code}"')
def step_enter_shipping_details(context, first_name, last_name, postal_code):
    context.checkout_page.enter_customer_info(first_name, last_name, postal_code)

@when('completes the purchase')
def step_complete_purchase(context):
    context.checkout_page.finish_purchase()
    context.confirmation_page = ConfirmationPage(context.driver)

@then('the confirmation message "{message}" should be displayed')
def step_verify_confirmation_message(context, message):
    assert message in context.confirmation_page.get_confirmation_message()
    context.driver.quit()
