from behave import *
import requests
from pages.users_page import UsersAPI


@given("the user gather the end url '{url}'")
def end_url(context, url):
    context.api_page = UsersAPI()
    context.api_page.set_url(url)

@when("the user send the API Get request")
def users_get(context):
    context.api_page.get_users_api()

@then("the get user api response status code should be {status}")
def users_status(context, status):
    assert context.api_page.get_response_status() == int(status), "There is issue with response status...."

@then("the get user api response text contains {data}")
def users_response(context, data):
    assert context.api_page.response_contains(data), "The response data is not matching with expected value"


#---Creating the new user----

@when("the user pass the below data to send POST API")
def get_inputs(context):
    data = {}
    for i in context.table:
        data[i['name']] = i['job']
    context.api_page.post_users_api(data)

@then("the post user api response status code should be {status}")
def post_resp(context,status):
    assert context.api_page.get_response_status() == int(status), "POST request status code...."

@then("the post user api response text contains '{value}'")
def post_resp_text(context,value):
    assert context.api_page.response_contains(value), "Post response data issue...."


#----Updating the created user----
@when("the user pass the below data to send PUT API")
def update_user(context):
    updated_data = {}
    for i in context.table:
        updated_data[i['updated_name']] = i['updated_job']
    context.api_page.put_users_api(updated_data)

@then("the put user api response status code should be {status}")
def status(context,status):
    assert context.api_page.get_response_status() == int(status), "PUT api status code issue..."

@then("the put user api response text contains '{text}'")
def response_text(context, text):
    assert context.api_page.response_contains(text), "PUT api resonse data issue..."


#-----Deleting the user record----
@when("the user send the delete api request")
def delete_req(context):
    context.api_page.delete_users_api()

@then("the delete user api status code should be {status}")
def delete_status(context, status):
    assert context.api_page.get_response_status() == int(status), "Delete api status code issue..."
