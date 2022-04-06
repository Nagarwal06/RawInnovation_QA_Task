Feature: Logged-in user can create note.
  Scenario: Create note
    Given User should be logged-in.
    When User clicks on create note
    When Add a note Tile and description
    When Click on Account Menu
    Then Click on Logout button