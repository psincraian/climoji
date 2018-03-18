Feature: search emojis that are similar to a given word

  Scenario: search emojis
    When I make a call to search with rockit
    Then I want to see the following
    """
    [1] 🚀  - :rocket:
    """
