from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given(u'User is logged as admin')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/login")
    context.driver.set_window_size(1896, 1000)
    context.driver.find_element(By.XPATH, "//*[@id='input-username']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-username']").send_keys("user")
    context.driver.find_element(By.XPATH, "//*[@id='input-password']").click()
    context.driver.find_element(By.XPATH, "//*[@id='input-password']").send_keys("bitnami")
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()

@given(u'is on admin Homepage')
def step_impl(context):
    pass

@when(u'admin clicks "Catalog"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()


@when(u'admin clicks "Products"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()

@given(u'is on product edit page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr[1]/td[7]/div/a").click()


@when(u'admin select "data" in top menu')
def step_impl(context):
   context.driver.find_element(By.XPATH, "//*[@id='form-product']/ul/li[2]").click()


@when(u'change product price value')
def step_impl(context):
    context.driver.find_element(By.ID, "input-price").send_keys("500.000")


@when(u'click "save"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/button").click()
    


@then(u'product price is changed')
def step_impl(context):
    pass
