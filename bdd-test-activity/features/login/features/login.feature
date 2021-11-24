Feature: Login

  Scenario: Valid Login (1a)
    Given a user in the login page
    When user insert they correctly credentials
    Then the user should be directed for homepage

    Scenario: Invalid Login (1b)
      Given user in the login page
      When user insert they invalid credentials
      Then system returns that the credentials are not valid