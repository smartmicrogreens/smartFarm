import socket

# Connection to Telnet server (ESP module)
def connect_to_module(_host, _port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)
    try:
        client.connect((_host, _port))
        print('Connected: {} ({})'.format(_host, _port))
    except:
        return False
    return client

def disconnect_from_module(_client):
    # Regarding shutdown, refer to https://docs.python.org/3/howto/sockets.html in "Disconnecting"
    _client.shutdown()
    _client.close()
