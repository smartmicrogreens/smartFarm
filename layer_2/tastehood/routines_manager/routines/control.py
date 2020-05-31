from routines_manager.core.module_connect import connect_to_module
from routines_manager.core.read_socket import send
from routines_manager.core.constants import EOL

HOST = '192.168.11.41'

def update_device(_head: str, _input: list, _host: str):
    client = connect_to_module(_host, 23)
    output = _head

    if _input is not None:
        for i in range(len(_input)-1):
            output += str(_input[i]) + ';'
        output += str(_input)[-2]
        output += EOL

    reply = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return reply

def read_output(_instruction: str, _host: str):
    client = connect_to_module(_host, 23)

    reply = send(client, _instruction)
    client.shutdown(0)
    client.close()
    return reply

# Test sentences
# from routines_manager.core.instructions import LIGHT_UPDATE_STATUS, LIGHT_READ_STATUS
# lights = [1,0,0,1]
# print(update_output(LIGHT_UPDATE_STATUS, lights, HOST))
# print(read_output(LIGHT_READ_STATUS, HOST))
# print(update_output('<2>', [],HOST))
