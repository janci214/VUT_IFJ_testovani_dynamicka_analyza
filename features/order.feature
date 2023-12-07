Feature: Items search and ordering

    Scenario: Search product from search bar 
        Given a web browser is at e-shop homepage 
        When customer searchs "iphone"
        Then page with following products is shown:
            | iPhone  |
    
    Scenario: Search in product description
        Given a web browser is at e-shop homepage 
        When customer searchs "iphone"
        And fill the "Search in product description" checkbox
        Then page with following products is shown:
            | iPhone     |
            | iPod Nano  |
            | iPod Touch |
    
    Scenario: User added new item to cart
        Given User is on page with selected item
        When User adds item to cart
        Then Cart contains one more item
    
    

    Scenario: Order with new address
        Given User is on checkout page
        And "I want to use new address" is selected
        When User fill required informations
        And select continue
        And confirm order
        Then customer is shown "Your order has been placed!"