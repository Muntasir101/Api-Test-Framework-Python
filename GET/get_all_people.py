import requests
from assertpy.assertpy import assert_that
from config import BASE_URI


def test_read_all():
    # We use requests.get() with url to make a get request
    response = requests.get(BASE_URI)
    # response from requests has many useful properties
    # we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    # We can get python dict as response by using .json() method
    response_text = response.json()

    print(response_text)
