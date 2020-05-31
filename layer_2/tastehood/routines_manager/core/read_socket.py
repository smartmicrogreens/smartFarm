import sys
import select

def send(_socket: 'socket', _instruction: bytes ):
    """ Send: Sends an instruction and returns the reply from device """
    _socket.send(_instruction)

    # Get socket info from stdin
    socket_list = [sys.stdin, _socket]
    # Read all standard sockets
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    # For every read
    for sock in read_sockets:
        # incoming message from remote server

        if sock == _socket:
            data = sock.recv(4096)
            data.decode('utf-8')
            if not data:
                return 99
            else:
                #print("last data: " + str(data))
                return data