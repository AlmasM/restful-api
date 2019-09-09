from helpers.env_loader import URL
from helpers.api_endpoints import GET_DEVICE_CREDS
from request_functions.post_request import post_request


def get_device_creds(headers={}, body={}):
    """Create device

    Returns:
        responseJson [json] -- API request reponse in the JSON format
    """

    url = '{}/{}'.format(URL, GET_DEVICE_CREDS)
    response = post_request(url, headers=headers, body=body)

    return response
