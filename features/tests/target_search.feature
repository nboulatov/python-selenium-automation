# Created by Nikita at 1/27/2024
Feature: Target.com search tests

  Scenario: User can see empty cart message
    Given I navigate to site: Target.com
    When I click icon: cart
    When I wait 2 seconds
    Then I verify message: Your cart is empty

  Scenario: Logged out user can access sign in page
    Given I navigate to site: Target.com
    When I click button: Sign in
    When I wait 2 seconds
    When I click link: Sign in
    When I wait 2 seconds
    Then I verify message: Sign into your Target account

  Scenario: User can see that an item has been added to the cart on the cart page
    Given I navigate to site: Target.com
    When I search: coffee
    When I wait 2 seconds
    When I click on product: coffee
    When I wait 2 seconds
    When I click button: Add to cart
    When I click button: View cart & check out
    When I wait 2 seconds
    Then I verify number of items in cart: 1 item