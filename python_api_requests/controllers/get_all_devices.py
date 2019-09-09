
from request_functions.get_request import get_request
from helpers.api_endpoints import GET_ALL_DEVICES
from helpers.env_loader import URL
import json
from requests.exceptions import HTTPError
import requests
import os
print(os.getcwd())


def get_all_devices():
    """Request device information given deviceId 

    Returns:
        responseJson [json] -- API request reponse in the JSON format
    """

    url = '{}/{}'.format(URL, GET_ALL_DEVICES)

    response = get_request(url)

    return response
