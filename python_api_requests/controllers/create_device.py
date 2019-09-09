from helpers.env_loader import URL
from helpers.api_endpoints import CREATE_DEVICE
from request_functions.put_request import put_request


def create_device(body=None):
    """Create device

    Returns:
        responseJson [json] -- API request reponse in the JSON format
    """

    url = '{}/{}'.format(URL, CREATE_DEVICE)
    print("For URL: {}".format(url))
    response = put_request(url, body=None)

    return response
