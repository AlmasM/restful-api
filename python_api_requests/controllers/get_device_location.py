from helpers.env_loader import URL
from helpers.api_endpoints import GET_DEVICE_LOCATION
from request_functions.post_request import post_request


def get_device_location(headers=None, body=None):
    """Create device

    Returns:
        responseJson [json] -- API request reponse in the JSON format
    """

    url = '{}/{}'.format(URL, GET_DEVICE_LOCATION)
    print("For URL: {}".format(url))
    response = post_request(url, headers=headers, body=None)

    return response
