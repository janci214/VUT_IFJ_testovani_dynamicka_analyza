Feature: Users administration

    Scenario: Display Users 
        Given User is logged as admin
        And is on admin Homepage
        When admin clicks two times on "Customers"
        Then all customers will show up

    Scenario: Edit user Name
        Given User is on customers page
        When admin clicks on "Edit"
        And change users name
        Then customer name is changed
    
    Scenario: Delete User 
        Given User is on customers page
        When select customers checkbox
        And click delete 
        Then customer is deleted

    Scenario: Log out
        Given User is logged as admin
        When user clicks "Logout"
        Then user is logged out