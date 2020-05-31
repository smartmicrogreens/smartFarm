from routines_manager.core.module_connect import connect_to_module
from routines_manager.core.read_socket import send
from routines_manager.core.instructions import LIGHT_UPDATE_STATUS, EOL

def update_light_status(_L1, _L2, _L3, _L4, _host):
    client = connect_to_module(_host, 23)
    output = LIGHT_UPDATE_STATUS + str(_L1) + ';' + str(_L2) + ';' + str(_L3) + ';' + str(_L4) + EOL
    #print(output)
    input = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return input

#print(update_light_status(0,1,1,0,'192.168.0.100'))

def update_light_status_2(_lights, _host):
    client = connect_to_module(_host, 23)
    output = LIGHT_UPDATE_STATUS
    for i in range(len(_lights)-1):
        output += str(_lights[i]) + ';'
    output += str(_lights.pop())
    output += EOL

    print(output)

    input = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return input

#lights = [1,0,1,0]
#print(update_light_status_2(lights,'192.168.0.100'))

def update_dehum_status(_status, _host):
    client = connect_to_module(_host, 23)
    output = LIGHT_UPDATE_STATUS + str(_L1) + ';' + str(_L2) + ';' + str(_L3) + ';' + str(_L4) + EOL
    #print(output)
    input = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return input


def update_airconditioner_status(_status, _host):
    client = connect_to_module(_host, 23)
    output = LIGHT_UPDATE_STATUS + str(_L1) + ';' + str(_L2) + ';' + str(_L3) + ';' + str(_L4) + EOL
    #print(output)
    input = send(client, bytes(output, 'ascii'))
    client.shutdown(0)
    client.close()
    return input