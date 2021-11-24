Feature: Edit Profile

  Scenario: Edit profile informations (1a)
    Given user in the Edit Profile page
    When fills out all the required informations and clicks in Save Profile
    Then system updates the informations


    Scenario: Change Password (1b)
      Given a user in the Edit Profile page
      When fills they current password and confirm you new password
      Then systems updates the password