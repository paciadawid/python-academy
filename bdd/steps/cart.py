from behave import *


@when("I navigate to cart")
def step_impl(context):
    context.cart_page.navigate_to_cart()


@then("I see empty cart")
def step_impl(context):
    assert context.cart_page.check_if_empty_cart()


@when("I add {number_of_items} items of {item_name} to the cart")
def step_impl(context, number_of_items, item_name):
