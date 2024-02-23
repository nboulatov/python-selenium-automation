# Created by Nikita at 1/27/2024
Feature: Target.com search tests

  Scenario: User can see empty cart message
    Given I navigate to site: Target.com
    When I click button: cart
    Then I verify message: Your cart is empty

  Scenario: User can access sign in page
    Given I navigate to site: Target.com
    When I click button: Sign in
    When I click link: Sign in
    Then I verify message: Sign into your Target account

  Scenario: User is able to login to a Target account
    Given I navigate to site: Target.com
    When I click button: Sign in
    When I click link: Sign in
    When I input username: poveto9067@fkcod.com
    When I input password: targetTarget1!
    When I click button: Sign in with password
#    When I click link: Skip
#    When I click button: Maybe later
    Then I verify login for: Target

  Scenario: User can see that an item has been added to the cart on the cart page
    Given I navigate to site: Target.com
    When I search: banana
    When I click on product: banana
    When I click button: Add to cart
    When I click button: View cart & check out
    Then I verify number of items in cart: 1

  Scenario: User can search for a specific product
    Given I navigate to site: Target.com
    When I search: coffee
    Then I see search results for: coffee
    Then I see URL contains text: coffee

  Scenario Outline: User adds the first searched product to the cart
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

  Scenario: Verify product's colors
    Given I navigate to product: A-81540287
    Then I verify product colors

  Scenario: Verify that every product has a name and image
    Given I navigate to site: Target.com
    When I search: coffee
    Then I verify that every product has a name and image

  Scenario: User can open and close Terms and Conditions from sign in page
    Given I navigate to site: Target.com
    When I click button: Sign in
    When I click link: Sign in
    When I store tab: original
    When I click link: Target terms and conditions
    When I switch to tab: new
    Then I see URL contains text: terms-conditions
    When I close tab: current
    When I switch to tab: original
    Then I see URL contains text: login?
