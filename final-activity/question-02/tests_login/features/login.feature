Feature: Login

  Scenario: Valid Login
    Given a user is in the SGME platform login page
    When the user insert they valid credentials
    Then system redirects the user to the homepage