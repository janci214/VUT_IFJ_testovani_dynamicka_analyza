Feature: Item and storage administration

    Scenario: Display orders
        Given User is logged as admin
        And is on admin Homepage
        When admin clicks "Sales"
        And admin clicks "Orders" 
        Then all products will show up

    Scenario: Confirm orders 
        Given is on orders page
        When admin clicks "View"
        And fill all required data
        And select "Confirm"
        Then selected order is confirmed 

    Scenario: Delete order 
        Give is on ordes page
        When admin selects checkbox on order 
        And click "Delete"
        Then selected order is deleted