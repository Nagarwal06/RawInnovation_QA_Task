Feature: Successful login and verify the note
  Scenario: Signin again and verify the saved note
    Given User is on signin page to verify
    When User enter email address and clicks continue to verify
    When User enter password and click signin to verify
    When click on the created note
    Then User verify the note
