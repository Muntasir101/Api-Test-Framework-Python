"""
In this API we can delete a person by passing in the person_id
So here is the flow:

    Create a new person
    Get the person id using read API
    Hit the delete endpoint and assert
"""
from json import dumps
from uuid import uuid4

import requests
from assertpy.assertpy import assert_that
from config import BASE_URI


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


def test_created_person_can_be_deleted():
    persons_last_name = create_new_person()

    peoples = requests.get(BASE_URI).json()
    newly_created_user = search_created_user_in(peoples, persons_last_name)[0]

    delete_url = f'{BASE_URI}/{newly_created_user["person_id"]}'
    response = requests.delete(delete_url)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
