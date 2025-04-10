Feature: Compra de un producto en SauceDemo

  Scenario: Usuario inicia sesión, agrega un producto y completa la compra
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the user should be redirected to the inventory page

    When the user adds "Sauce Labs Backpack" to the cart
    And proceeds to checkout
    And enters shipping details "Juan" "Pérez" "12345"
    And completes the purchase
    Then the confirmation message "Thank you for your order!" should be displayed
