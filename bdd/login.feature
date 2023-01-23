# Created by dejve at 1/23/2023
Feature: Login

  Scenario: Successful login
    When I try to login with email seleniumremote@gmail.com and password tester
    Then I'm logged in

  Scenario: Wrong password
    When I try to login with email seleniumremote@gmail.com and password nietester
    Then I'm logged out

  Scenario: Empty password
    When I try to login with email seleniumremote@gmail.com and password _
    Then I'm logged out

  Scenario Outline: Login success check

    When I try to login with email <email> and password <password>
    Then I'm logged <status>

    Examples:
      | email                    | password  | status |
      | seleniumremote@gmail.com | tester    | in     |
      | seleniumremote@gmail.com | nietester | out    |
      | seleniumremote@gmail.com | _         | out    |