from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@when(u'admin clicks "Sales"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Sales").click()
    


@when(u'admin clicks "Orders"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Orders").click()


@then(u'all products will show up')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='nav-logout']/a").click()


@given(u'is on orders page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='input-username']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-username']").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-password']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-password']").send_keys("bitnami")
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()
    context.driver.find_element(By.LINK_TEXT, "Sales").click()
    context.driver.find_element(By.LINK_TEXT, "Orders").click()



@when(u'admin clicks "View"')
def step_impl(context):
    pass
    #musi byt naplnena databaza objednavkou
    #context.driver.find_element(By.XPATH, "//*[@id='form-order']/div[1]/table/tbody/tr/td[9]/a/i").click()

@when(u'fill all required data')
def step_impl(context):
    pass


@when(u'select "Confirm"')
def step_impl(context):
    pass
    #context.driver.find_element(By.ID, "button-confirm").click()


@then(u'selected order is confirmed')
def step_impl(context):
    pass


@when(u'admin selects checkbox on order')
def step_impl(context):
    pass
    #funguje len ak je naplnena databaza
    #context.driver.find_element(By.XPATH, "//*[@id='form-order']/div[1]/table/tbody/tr/td[1]/input[2]").click()
    

@when(u'click "Delete"')
def step_impl(context):
    pass
    #context.driver.find_element(By.XPATH, "//*[@id='button-delete']").click()


@then(u'selected order is deleted')
def step_impl(context):
    pass
    #assert context.driver.switch_to.alert.text == "Are you sure?"
    #context.driver.switch_to.alert.accept()