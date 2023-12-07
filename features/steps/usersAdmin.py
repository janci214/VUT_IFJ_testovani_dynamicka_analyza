from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



@when(u'admin clicks two times on "Customers"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Customers").click()
    context.driver.find_element(By.CSS_SELECTOR, "#collapse-5 > li:nth-child(1) > a").click()


@then(u'all customers will show up')
def step_impl(context):
    pass

@given(u'User is on customers page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#collapse-5 > li:nth-child(1) > a").click()

@when(u'admin clicks on "Edit"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='form-customer']/div[1]/table/tbody/tr[1]/td[7]/div/a").click()


@when(u'change users name')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='input-firstname']").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("uzivatel")

@then(u'customer name is changed')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/button").click()


@when(u'select customers checkbox')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='form-customer']/div[1]/table/tbody/tr[1]/td[1]/input").click()
    

@when(u'click delete')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/button[2]/i").click()

@then(u'customer is deleted')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Are you sure?"
    context.driver.switch_to.alert.accept()
    context.driver.find_element(By.XPATH, "//*[@id='nav-logout']/a").click()
    

@when(u'user clicks "Logout"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='nav-logout']/a").click()


@then(u'user is logged out')
def step_impl(context):
    pass
