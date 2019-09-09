from helpers.env_loader import URL
from helpers.api_endpoints import DELETE_DEVICE
from request_functions.delete_request import delete_request


def delete_device(headers={}, body={}):
    """Delete device

    Returns:
        responseJson [json] -- API request reponse in the JSON format
    """

    url = '{}/{}'.format(URL, DELETE_DEVICE)
    print("For URL: {}".format(url))
    response = delete_request(url, headers=headers, body=None)

    return response
