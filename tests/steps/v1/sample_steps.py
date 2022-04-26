from behave import given, when, then
import logging.config
#from gaji_gesa_api_python_utils.dataclasses.v2.profile.gaji_gesa_profile import *
# from test_automation_python_utils.endpoints.gaji_gesa.gaji_gesa import *

logging.config.fileConfig('config/logging.ini')


def set_up_profile_request(context):
    v2_create_profile_request = GGCreateProfileRequest(
        authorization="Bearer 3992b1450ea2fdb2a0d41253b84f4fe9547cde91afad56d110fc44b50793ff84",
    )

    context.data["v2_create_profile_request"] = v2_create_profile_request


def delegate_profile_create_request(context):
    context.data["maya_credit_get_statement_response"] = create_profile_account(
        context.data["v2_create_profile_request"],
        validate_status=False)


@given("I want to test gaji gesa app")
def print_test(context):
    print("my first test")


@given("I want to create a user in the Gaji Gesa")
def create_profile_request(context):
    set_up_profile_request(context)
    context.data["test"] = "value from context"


@when("a user submit profile create request")
def submit_request(context):
    delegate_profile_create_request(context)


@then("profile is created")
def validate_profile_created(context):
    pass
