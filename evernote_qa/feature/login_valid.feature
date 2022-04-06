Feature: Successful login using email/password
  Scenario: Login with valid credentials
    Given Navigate to login page.
    When We enter valid email and password
    Then click on continue button
    Then verify user is logged-in.
