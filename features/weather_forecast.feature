Feature: Weather Forecast
  As an user,
  I want to go to Forecast Weather,
  So I can learn the weather of following days.

  Scenario: Go to Weather Forecast
    Given the user is in Disclaimer screen
    When the user clicks Agree button on disclaimer screen
    And the user is redirected to Privacy Policy Statements screen
    And the user clicks Agree button on Privacy Policy Statements screen
    And the user is redirected to News screen
    And the user clicks Next button 4 times
    And the user is redirected to Home screen
    And the user clicks Navigate Up Button
    And the user clicks "9-Day Forecast" from Left Drawer
    Then the user is redirected to Weather Forecast screen

#    There will be a failed test case on purpose for demonstration
  Scenario Outline: Learn the weather of following days
    Given the user is in Disclaimer screen
    When the user clicks Agree button on disclaimer screen
    And the user is redirected to Privacy Policy Statements screen
    And the user clicks Agree button on Privacy Policy Statements screen
    And the user is redirected to News screen
    And the user clicks Next button 4 times
    And the user is redirected to Home screen
    And the user clicks Navigate Up Button
    And the user clicks "9-Day Forecast" from Left Drawer
    And the user is redirected to Weather Forecast screen
    And the user scrolls to next <day>
    Then the user sees the forecast weather for <day>
    Examples:
      | day      |
      | Saturday |
      | grabled  |