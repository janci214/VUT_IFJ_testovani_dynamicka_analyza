from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@given(u'User is on registration page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/register")


@given(u'required fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("user")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("user")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("user.user@user.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("user")


@given(u'"I have read and agree to the Privacy Policy" box is checked')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when(u'customer clicks on "Continue"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()

@then(u'customer is shown:  "Your Account Has Been Created!"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Continue").click()

    context.driver.find_element(By.LINK_TEXT, "My Account").click()
    context.driver.find_element(By.LINK_TEXT, "Logout").click()
    context.driver.find_element(By.LINK_TEXT, "Continue").click()

@given(u'User is on login page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/login")
    context.driver.set_window_size(1228, 1144)


@given(u'enters his e-mail address')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("user.user@user.com")


@given(u'enters correct password')
def step_impl(context):
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("user")


@when(u'user clicks "Login"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()


@then(u'user is logged in')
def step_impl(context):
    pass    


@given(u'User is logged in first time')
def step_impl(context):
    pass


@given(u'is on any page of eshop')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")
    context.driver.set_window_size(1228, 1144)


@when(u'user clicks "MyAccount"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()

@when(u'clicks "Order history"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()


@then(u'order history is shown and empty')
def step_impl(context):
     context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'User is on any eshop page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='logo']/a/img").click()

@given(u'dropmenu for "My Account" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a/i[2]").click()
    
@when(u'customer clicks on "Logout"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()

@then(u'customer is shown page: "Account Logout"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Continue").click()