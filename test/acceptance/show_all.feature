Feature: show all emojis

  Scenario: show all emojis
    When I make a call to all
    Then I want to see the following
    """
    [1] 🥇  - :1st_place_medal:
    [2] 🥈  - :2nd_place_medal:
    [3] 🥉  - :3rd_place_medal:
    [4] 🆎  - :AB_button_(blood_type):
    [5] 🏧  - :ATM_sign:
    [6] 🅰  - :A_button_(blood_type):
    [7] 🇦🇫  - :Afghanistan:
    [8] 🇦🇱  - :Albania:
    [9] 🇩🇿  - :Algeria:
    [10] 🇦🇸  - :American_Samoa:
    """