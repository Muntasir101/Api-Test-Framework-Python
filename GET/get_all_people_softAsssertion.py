import requests
from assertpy.assertpy import assert_that, soft_assertions
from config import BASE_URI


def test_read_all_has_kent():
    # We use requests.get() with url to make a get request
    response = requests.get(BASE_URI)
    # response from requests has many useful properties
    # we can assert on the response status code

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.no_content)  # fails
        # We can get python dict as response by using .json() method
        response_content = response.json()

        # Use assertpy's fluent assertions to extract all fnames and then see the result is non empty and has
        # Kent in it.
        assert_that(response_content).extracting('fname').is_not_empty().does_not_contain('Kent')  # fails
