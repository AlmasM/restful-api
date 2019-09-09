from rest_http_functions.database.device import deviceDb


"""Get location of the device
Input:
    string -- deviceId of the device for which location is being requested
Returns:
    boolean -- boolean value indicating if element was removed
"""


def verify_location(deviceId):

    lat = deviceDb[deviceId]["currLocation"]["lat"]
    lon = deviceDb[deviceId]["currLocation"]["lon"]

    return lat, lon


"""Check if device in DB, and remove device from the DB
Input:
    string -- deviceId that needs to be removed
Returns:
    boolean -- boolean value indicating if element was removed
"""


def remove_device(deviceId):
    if deviceId in deviceDb:

        deviceDb.pop(deviceId)
        return True
    else:
        return False


"""Check if device in DB, and add device to the DB
Input:
    deviceId [string] -- deviceId that needs to be added
    devicePasscode [string] -- devicePasscode for the device
    deviceLocation [dict] - dictionary with "lat" and "lon" elements 
Returns:
    boolean -- boolean value indicating if element was added
"""


def add_device(deviceId, devicePasscode, deviceLocation):

    deviceObject = {}
    if deviceId in deviceDb:
        return False
    else:
        deviceObject["currLocation"] = deviceLocation
        deviceObject["devicePasscode"] = devicePasscode

        deviceDb.update({deviceId: deviceObject})
        return True


"""Verify if requested device exists in DB and credentials are valid

Input:
    deviceId [string] -- deviceId that needs to be verified
    devicePasscode [string] -- devicePasscode for the device
    
Returns:
    boolean -- boolean value indicating if element was verified
"""


def verify_device(deviceId, devicePasscode):
    # TODO verify if device is valid

    if deviceId in deviceDb:
        if devicePasscode in deviceDb[deviceId]["devicePasscode"]:
            return True
        else:
            return False
    else:
        return False
