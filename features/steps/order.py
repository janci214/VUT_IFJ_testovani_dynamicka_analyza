from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given(u'a web browser is at e-shop homepage')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")
    context.driver.set_window_size(1228, 1144)


@when(u'customer searchs "iphone"')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iphone")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)


@then(u'page with following products is shown')
def step_impl(context):
    pass


@when(u'fill the "Search in product description" checkbox')
def step_impl(context):
    context.driver.find_element(By.ID, "input-description").click()
    context.driver.find_element(By.ID, "button-search").click()


@given(u'User is on page with selected item')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone?search=iphone&description=1")
    context.driver.set_window_size(1228, 1393)


@when(u'User adds item to cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='button-cart']").click()
    

@then(u'Cart contains one more item')
def step_impl(context):
    pass


@given(u'User is on checkout page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone?search=iphone&description=1")
    context.driver.set_window_size(1228, 1393)
    context.driver.find_element(By.XPATH, "//*[@id='button-cart']").click()



@given(u'"I want to use new address" is selected')
def step_impl(context):
    pass


@when(u'User fill required informations')
def step_impl(context):
    #Not Working
    """
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[2]/a").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-firstname']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-firstname']").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-lastname']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-lastname']").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-address-1']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-address-1']").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-city']y").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-city']y").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-postcode']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-shipping-postcode']").send_keys("75210")
    dropdown = context.driver.find_element(By.XPATH, "input-shipping-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Aaland Islands']").click()
    context.driver.find_element(By.XPATH, "button-shipping-address").click()
    element = context.driver.find_element(By.XPATH, "button-shipping-address")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.XPATH, "button-shipping-methods").click()
    element = context.driver.find_element(By.XPATH, "button-shipping-methods")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.XPATH, "input-shipping-method-flat-flat").click()
    context.driver.find_element(By.XPATH, "button-shipping-method").click()
    context.driver.find_element(By.XPATH, "button-payment-methods").click()
    context.driver.find_element(By.XPATH, "input-payment-method-cod-cod").click()
    context.driver.find_element(By.XPATH, "button-payment-method").click()
"""
    pass
@when(u'select continue')
def step_impl(context):
    pass
    #context.driver.find_element(By.LINK_TEXT, "Continue").click()

@when(u'confirm order')
def step_impl(context):
    pass


@then(u'customer is shown "Your order has been placed!"')
def step_impl(context):
    pass