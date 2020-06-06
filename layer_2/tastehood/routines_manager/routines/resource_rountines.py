""" Set of commands to execute by scheduler """
import time
import click

from routines_manager.core.iot_device import *

@click.command()

def switch_status(property: tuple, shelf, status: bool, device: 'IotDevice'):

    device.connect()

    # Property refer to which resource you are going to modify.
    # i.e. _property -> LIGHT: tuple = ( LIGHT_READ_STATUS, LIGHT_UPDATE_STATUS )
    cur_status = device.read(property[0])
    # print("Current st = " + str(cur_status))
    new_status = cur_status
    print(new_status)
    if status:
        # Case True: Change to 'ON' only if it is 'OFF'
        if cur_status[shelf] == 0:
            new_status[shelf] = 1
    else:
        # Case True: Change to 'ON' only if it is 'ON'
        if cur_status[shelf] == 1:
            new_status[shelf] = 0

    print(new_status)
    device.update(property[1], new_status)
    device.disconnect()

