# Created by dejve at 1/30/2023
Feature: Cart
  # Enter feature description here

  @smoke @logged @checkout
  Scenario: Add item to cart and check total cost
    # Enter steps here

  @unlogged
  Scenario: Check empty cart
    Given I'm logged out
    When I navigate to cart
    Then I see empty cart

  @smoke @unlogged
  Scenario: Adding to cart negative number of items
    Given I'm logged out
    When I add -1 items of unicorn to the cart
    And I navigate to cart
    Then I see empty cart

  @unlogged
  Scenario: Adding to cart 0 items
    Given I'm logged out
    When I add 0 items of unicorn to the cart
    And I navigate to cart
    Then I see empty cart

  @unlogged @checkout
  Scenario: Proceed to checkout as unlogged user
    Given I'm logged out
    When I add 1 items of unicorn to the cart
    When I navigate to cart
    And I proceed to checkout
    Then I see login modal

  @smoke @unlogged
  Scenario: Removing items from cart