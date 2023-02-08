"""
Here is the complete flow that we want to automate:

    Create a new person in the db
    Verify if the newly created user is present using the GET API
    Filter to find if the created data is present in all the users in the system

"""
from json import dumps
from uuid import uuid4

import requests
from assertpy.assertpy import assert_that
from config import BASE_URI


def test_new_person_can_be_added():
    unique_last_name = create_new_person()

    # After user is created, we read all the users and then use list comprehension to find if the
    # created user is present in the response list
    peoples = requests.get(BASE_URI).json()
    is_new_user_created = search_created_user_in(peoples, unique_last_name)
    assert_that(is_new_user_created).is_not_empty()


def create_new_person():
    # Ensure a user with a unique last name is created everytime the test runs
    # Note: json.dumps() is used to convert python dict to json string
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'New',
        'lname': unique_last_name
    })

    # Setting default headers to show that the client accepts json
    # And will send json in the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # We use requests.post method with keyword params to make the request more readable
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name


def search_created_user_in(peoples, last_name):
    return [person for person in peoples if person['lname'] == last_name]
