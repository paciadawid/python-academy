from behave import step, then, when


@when("I try to login with email {email} and password {password}")
def login(context, email, password):
    if password == "_":
        password = ""
    context.login_page.login_using_email_password(email, password)


@then("I'm logged in")
def check_login(context):
    assert context.login_page.check_if_logged_in()


@step("I'm logged out")
def check_logout(context):
    assert not context.login_page.check_if_logged_in()


@then("I'm logged {status}")
def check_login_status(context, status):
    success = context.login_page.check_if_logged_in()
    if status == "in":
        assert success
    elif status == "out":
        assert not success
    else:
        raise KeyError("Choose between 'in' and 'out'")
