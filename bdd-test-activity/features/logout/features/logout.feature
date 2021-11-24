Feature: Logout

  Scenario: Sign out to the platform (2a)
    Given user be logged in the platform
    When they click in Sign Out
    Then Then the user should be redirected for login page