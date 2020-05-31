from routines_manager.core.module_connect import connect_to_module
from routines_manager.core.read_socket import send
from routines_manager.core.constants import ENV_READ_STATUS
from routines_manager.core.iot_device import IotDevice

def scan_environment(_host):
    device = IotDevice('ESP module', 'First shelf ever device', '192.168.0.100')
    client = connect_to_module(_host, 23)
    device.connect()
    data = send(client, ENV_READ_STATUS).split(b';')
    print(data)
    instruction = data[0]

    if instruction.decode('utf-8') == '0':
        # temperature, humidity = data.split(b';')[1:]
        env_val = { "temperature": data[1],
                    "humidity": data[2],
                    "soil_moisture": -1,
                    "water_consumption": -1,
                    "energy_consumption": -1 }

        # for x in env_val:
        #     print(env_val[x])

        return env_val
        device.disconnect()
    else:
        # Returning -1, -1 in order to request the webserver to nullify the values on DB.
        return -1. -1



# Test enviroment scan
print(scan_environment('192.168.0.100'))