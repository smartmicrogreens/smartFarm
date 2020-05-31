""" Set of commands to execute by scheduler """
import time

#from routines_manager.routines.control import update_output, read_output
from routines_manager.core.constants import *
from routines_manager.core.iot_device import *

# 1. Sunrise / Sunset
def switch_light_status(_shelf, _switchOn: bool, _device: 'IotDevice'):

    _device.connect()

    cur_status = _device.read(LIGHT_READ_STATUS)
    # print("Current st = " + str(cur_status))
    new_status = cur_status
    print(new_status)
    if _switchOn:
        # Case True: Change to 'ON' only if it is 'OFF'
        if cur_status[_shelf] == 0:
            new_status[_shelf] = 1
    else:
        # Case True: Change to 'ON' only if it is 'ON'
        if cur_status[_shelf] == 1:
            new_status[_shelf] = 0

    print(new_status)
    _device.update(LIGHT_UPDATE_STATUS, new_status)
    _device.disconnect()

device = IotDevice('myDevice', 'This is my device', '192.168.11.41')
switch_light_status(SHELF_2, OFF, device)