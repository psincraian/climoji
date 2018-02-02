Feature: show given emoji alias

  Scenario: show given emoji to the terminal
    When I make a call to show with :smile:
    Then I want to see the following
    """
    😄
    """

  Scenario: show emoji not found when alias does not exist
    When I make a call to show with :not-found:
    Then I want to see the following
    """
    Emoji ":not-found:" not found
    """
