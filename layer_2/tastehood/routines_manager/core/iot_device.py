import socket
from routines_manager.core.module_connect import connect_to_module
from routines_manager.core.read_socket import send
from routines_manager.core.constants import EOL

# For now it uses standard Telnet port to communicate to device
PORT = 23

class IotDevice:

    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id    # Currently is IP address but could change.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isConnected = False

    def get_device_name(self):
        return self.name

    def get_device_description(self):
        return self.description

    def get_device_ip(self):
        return self.id

    def connect(self):
        if not self.isConnected:
            self.client.settimeout(2)
            try:
                self.client.connect((self.id, PORT))
                print('Connected: {} ({})'.format(self.id, PORT))
                self.isConnected = True
            except:
                return False
            return self.client

    def disconnect(self):
        if self.isConnected:
            # Regarding shutdown, refer to https://docs.python.org/3/howto/sockets.html in "Disconnecting"
            self.isConnected = False
            self.client.shutdown(0)
            self.client.close()

    def update(self, _head: str, _input: list):

        #client = connect_to_module(_host, 23)

        # Generates '<_head;val1;val2;...;val3>'
        output = _head
        if _input is not None:
            for i in range(len(_input) - 1):
                output += str(_input[i]) + ';'
            output += str(_input)[-2]
            output += '>'

        reply = send(self.client, bytes(output, 'ascii'))
        return reply

    def read(self, _instruction):
        #client = connect_to_module(_host, 23)
        reply = send(self.client, bytes(_instruction, 'ascii'))

        output = reply.split(b'>')[0] # Discards '>'
        output = output.split(b';')[1:] # Separates ';' and discards '<'
        output_2 = []
        for x in output:
            output_2.append(int(x.decode('utf-8')))

        return output_2

# device = IotDevice('myDevice', 'This is my device', '192.168.11.41')
#
# device.connect()
# print(device.update('<2;', [0,1,1,0]))
# print(device.read('<0>'))
# device.disconnect()

