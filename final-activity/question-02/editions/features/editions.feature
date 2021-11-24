Feature: Editions

  Scenario: Search a existent edition
    Given a user is in the Editions page
    When the user inserts the existent edition name and clicks in Search
    Then the system shows the edition
