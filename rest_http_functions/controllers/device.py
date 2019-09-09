from flask import Flask, request, Blueprint
from rest_http_functions.database.device import deviceDb
from rest_http_functions.helpers.device import verify_device, verify_location, remove_device, add_device
import json

device = Blueprint('device', __name__)


@device.route('/all', methods=['GET', 'POST'])
def all_devices():
    """Get all the devices in the DB

    - Request Methods: GET, POST
    - Header: None
    - Body: None 
    Returns:
        dict -- response which contains 2 dicts: statusCode, body
    """

    statusCode = 400
    body = {}
    response = {"statusCode": statusCode, "body": body}

    if request.method == "GET" or request.method == "POST":

        allDevices = list(deviceDb.keys())

        body.update({"allDevices": allDevices})
        response["statusCode"] = 200

        return response
    else:
        return response


@device.route('/device', methods=['GET', 'POST'])
def device_creds():
    """Verify if credentials provided are valid for the device

    - Request Methods: POST
    - Header: None
    - Body: 
        {
            "deviceId": "deviceIdString" ,
            "devicePasscode": "devicePasscodeString"
        }
    Returns:    
        dict -- response which contains 2 dicts: statusCode, body
    """

    statusCode = 400
    body = {}
    response = {"statusCode": statusCode, "body": body}

    if request.method == "POST":
        requestContent = request.json

        deviceId = requestContent["deviceId"]
        devicePasscode = requestContent["devicePasscode"]
        isValid = verify_device(deviceId, devicePasscode)

        body.update({"isValid": isValid})
        response["statusCode"] = 200

        return response
    else:
        return response


@device.route('/location', methods=['GET', 'POST'])
def device_location():
    """Get location of the device

    - Request Methods: POST
    - Header: 
        {
            "deviceId": "deviceIdString"
        }
    - Body: None
    Returns:    
        dict -- response which contains 2 dicts: statusCode, body
    """

    statusCode = 400
    body = {}
    response = {"statusCode": statusCode, "body": body}

    if request.method == "POST":
        requestContent = request.headers
        deviceId = requestContent["deviceId"]

        lat, lon = verify_location(deviceId)

        body.update({"deviceId": deviceId, "lat": lat, "lon": lon})
        response["statusCode"] = 200

        return response
    else:
        return response


@device.route('/create', methods=['PUT'])
def create_device():
    """Create new device in the DB

    - Request Methods: PUT
    - Header: None
    - Body: 
        {
        "deviceId": "deviceIdString",
        "devicePasscode": "devicePasscodeString",
        "currLocation": {
            "lat": 12345,
            "lon": 54321
            }
        }
    Returns:    
        dict -- response which contains 2 dicts: statusCode, body
    """

    statusCode = 400
    body = {}
    response = {"statusCode": statusCode, "body": body}

    if request.method == "PUT":
        requestContent = request.json

        deviceId = requestContent["deviceId"]
        devicePasscode = requestContent["devicePasscode"]
        deviceLocation = requestContent["currLocation"]

        isAdded = add_device(deviceId, devicePasscode, deviceLocation)

        body.update({"isAdded": isAdded})

        response["statusCode"] = 200

        print(deviceDb)
        return response
    else:
        return response


@device.route('/delete', methods=['DELETE'])
def delete_device():
    """Delete a device from the DB

    - Request Methods: PUT
    - Header:         
        {
            "deviceId": "deviceIdString"
        }
    - Body: None
    Returns:    
        dict -- response which contains 2 dicts: statusCode, body
    """

    statusCode = 400
    body = {}
    response = {"statusCode": statusCode, "body": body}

    if request.method == "DELETE":
        requestContent = request.headers
        deviceId = requestContent["deviceId"]

        isDeleted = remove_device(deviceId)

        body.update({"isDeleted": isDeleted})

        response["statusCode"] = 200

        print(deviceDb)
        return response
    else:
        return response
