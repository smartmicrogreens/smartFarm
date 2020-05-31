from routines_manager.core.module_connect import connect_to_module
from routines_manager.core.read_socket import send
from routines_manager.core.instructions import LIGHT_UPDATE_STATUS, EOL

HOST = '192.168.11.41'

# def update_light_status(_input, _host):
#     client = connect_to_module(_host, 23)
#     output = LIGHT_UPDATE_STATUS
#     for i in range(len(_input)-1):
#         output += str(_input[i]) + ';'
#     output += str(_input.pop())
#     output += EOL
#
#     print(output)
#
#     input = send(client, bytes(output, 'ascii'))
#     client.shutdown(0)
#     client.close()
#     return input

def update_output(_head: str, _input: list, _host: str):
    client = connect_to_module(_host, 23)
    output = _head

    if _input is not None:
        for i in range(len(_input)-1):
            output += str(_input[i]) + ';'
        output += str(_input)[-2]
        output += EOL

    input = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return input

lights = [1,0,0,1,0,0,0,0]
print(update_output(LIGHT_UPDATE_STATUS, lights, HOST))
#print(update_output('<2>', [],HOST))
