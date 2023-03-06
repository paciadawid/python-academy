from behave import step, then, when


@when("I navigate to cart")
def navigate_to_cart(context):
    context.cart_page.navigate_to_cart()


@then("I see empty cart")
def check_empty_cart(context):
    assert context.cart_page.check_if_empty_cart()


@when("I add {number_of_items} items of {item_name} to the cart")
def step_impl(context, number_of_items, item_name):
    context.products_page.search_product(item_name)
    context.products_page.view_product()
    context.product_details_page.add_to_cart(number_of_items)


@step("I proceed to checkout")
def go_to_checkout(context):
    context.cart_page.proceed_to_checkout()


@then("I see login modal")
def modal_check(context):
    context.cart_page.check_if_login_modal_visible()
