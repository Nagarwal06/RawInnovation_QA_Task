Feature: Unsuccessful login using inavlid password
  Scenario: Login with invalid credentials
    Given Navigate to login page
    When We enter valid email and click continue
    When We enter invalid password and click continue
    Then Error message should be displayed.
