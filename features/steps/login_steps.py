from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.driver.get("https://www.saucedemo.com")
    context.login_page = LoginPage(context.driver)

@when('the user logs in with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)

@when('the user logs in with invalid credentials')
def step_when_user_logs_in_invalid(context):
    context.login_page.login("invalid_user", "invalid_password")

@when('the user logs in with empty credentials')
def step_when_user_logs_in_empty(context):
    context.login_page.login("", "")

@then('the user should be redirected to the inventory page')
def step_then_inventory_page(context):
    assert context.inventory_page.is_inventory_page_displayed()

@then('an error message should be displayed')
def step_then_error_message(context):
    assert "Epic sadface" in context.login_page.get_error_message()
