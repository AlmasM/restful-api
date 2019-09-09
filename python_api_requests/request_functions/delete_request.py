
import requests
from requests.exceptions import HTTPError
import json


def delete_request(url, headers={}, body={}):
    """Make request to an API endpoint given URL

    Arguments:
        url {string} -- API endpoint

    Returns:
        [json] -- response in the JSON format
    """

    try:

        response = requests.delete(url, headers=headers, data=body)

        responseJson = json.dumps(response.json())

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))
    except Exception as err:
        print('Other error occurred: {}'.format(err))
    else:

        return responseJson
