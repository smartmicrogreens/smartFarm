import socket

# For now it uses standard Telnet port to communicate to device
PORT = 23

class IotDevice:
    def __init__(self, name, description, ip_address):
        self.name = name
        self.description = description
        self.ip_address = ip_address
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_device_name(self):
        return self.name

    def get_device_description(self):
        return self.description

    def get_device_ip(self):
        return self.ip_address

    def connect(self):

        self.client.settimeout(2)
        try:
            self.client.connect((self.ip_address, PORT))
            print('Connected: {} ({})'.format(self.ip_address, PORT))
        except:
            return False
        return self.client

    def disconnect(self):
        # Regarding shutdown, refer to https://docs.python.org/3/howto/sockets.html in "Disconnecting"
        self.client.shutdown()
        self.client.close()


