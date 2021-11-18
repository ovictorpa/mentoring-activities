Feature: Login

  Scenario: Valid Login (1a)
    Given a user in the login page
    When user insert they correctly credentials
    Then the user should be directed for homepage