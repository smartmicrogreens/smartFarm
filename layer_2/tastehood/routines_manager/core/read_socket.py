import sys
import select
from routines_manager.core.module_connect import connect_to_module
# Constant definition
# - By sending the instruction '0', the ESP modulo will reply with temperature and humidity
# SCAN_INSTR = b'<0>'

def send(_socket, _instruction: str):
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
                return data