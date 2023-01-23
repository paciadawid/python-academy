from behave import *


@when('I try to login with email {email} and password {password}')
def step_impl(context, email, password):
    if password == "_":
        password = ""
    context.login_page.login_using_email_password(email, password)


@then("I'm logged in")
def step_impl(context):
    assert context.login_page.check_if_logged_in()


@then("I'm logged out")
def step_impl(context):
    assert not context.login_page.check_if_logged_in()


@then("I'm logged {status}")
def step_impl(context, status):
    success = context.login_page.check_if_logged_in()
    if status == "in":
        assert success
    elif status == "out":
        assert not success
    else:
        raise KeyError("Choose between 'in' and 'out'")
