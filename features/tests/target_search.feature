# Created by Nikita at 1/27/2024
Feature: Target.com search tests

  Scenario: User can see empty cart message
    Given I navigate to site: Target.com
    When I click icon: cart
    Then I verify message: Your cart is empty

  Scenario: Logged out user can access sign in page
    Given I navigate to site: Target.com
    When I click button: Sign in
    When I click link: Sign in
    Then I verify message: Sign into your Target account

  Scenario: User can see that an item has been added to the cart on the cart page
    Given I navigate to site: Target.com
    When I search: coffee
    When I click on product: coffee
    When I click button: Add to cart
    When I click button: View cart & check out
    Then I verify number of items in cart: 1 item

  Scenario Outline: User can search for a product on Target.com
    Given I navigate to site: Target.com
    When I search: <product>
    When I click on product: <product>
    When I click button: Add to cart
    When I click button: View cart & check out
    Then I verify number of items in cart: 1 item

    Examples:
      | product      |
      | coffee       |
      | tennis balls |

  Scenario: Verify Target.com's header
    Given I navigate to site: Target.com
    Then I verify: header

  Scenario: Verify 5 benefit boxes on Target.com/circle page
    Given I navigate to site: Target.com/circle
    Then I verify number of benefits: 5 benefits

  Scenario: Verify UI elements on https://help.target.com/help page
    Given I navigate to site: https://help.target.com/help
    Then I verify UI elements on Target Help page

  Scenario: Verify colors
    Given I navigate to product: A-81540287
    Then I verify product's colors

  Scenario: Verify that every product has a name and image after search
  Given I navigate to site: Target.com
  When I search: coffee
  Then I verify that every product has a name and image