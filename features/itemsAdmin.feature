Feature: Item and storage administration

    Scenario: Display products
        Given User is logged as admin
        And is on admin Homepage
        When admin clicks "Catalog"
        And admin clicks "Products" 
        Then all products will show up


     Scenario: Edit price of product
        Given User is logged as admin
        And is on product edit page
        When admin select "data" in top menu
        And change product price value
        And click "save"
        Then product price is changed 

