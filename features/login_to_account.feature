Feature: I want to sign in to my account



  Scenario: sign in on exist account
    Given the user go to login site
    When customer log in with email "qa+test@wp.pl" and password "T123456"
    Then customer is on "moje-konto" site
#    When the user enter to search bar words "psi patrol" and see hint
#    And the user click on search button
#    Then the user is on search site with url "szukaj"
#    And the text in header of search is "psi patrol"
#    And the user see list of products after click on search button
#    And amount displayed product is equal with amount in hint