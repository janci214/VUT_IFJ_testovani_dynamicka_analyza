Feature: Customer registration and order history
    
    Scenario: Registration of new customer - Valid registration 
        Given User is on registration page
        And required fields are filled
        And "I have read and agree to the Privacy Policy" box is checked
        When customer clicks on "Continue"
        Then customer is shown:  "Your Account Has Been Created!"

    Scenario: User logs into account
        Given User is on login page
        And enters his e-mail address
        And enters correct password
        When user clicks "Login"
        Then user is logged in
    
    Scenario: View empty order historyclear
        Given User is logged in first time
        And is on any page of eshop
        When user clicks "MyAccount"
        And clicks "Order history"
        Then order history is shown and empty


    Scenario: Logging-out 
        Given User is on any eshop page
        And dropmenu for "My Account" is shown
        When customer clicks on "Logout"
        Then customer is shown page: "Account Logout"