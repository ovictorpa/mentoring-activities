Feature: Glossary

  Scenario: Search a existent word (2a)
    Given a user in the Glossary page
    When they inserts the existent word and clicks in Search
    Then the system shows the word and the concept

    Scenario: Search a nonexistent word (2b)
      Given the user in the Glossary page
      When they inserts the nonexistent word and clicks in Search
      Then the system shows a not found message