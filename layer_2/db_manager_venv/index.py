import socket
import sys, select, string
import mysql.connector
from datetime import datetime
import time

instruction = 99
temperature = 10
humidity = 10

# MySQL configuration information
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'microgadmin',
    passwd = 'Hostname.123',
    database = "microg"
)

# Socket configuration information
HOST = '192.168.0.100'
#HOST = '192.168.11.41'
PORT = 23

# MySQL connection attempt
mycursor = mydb.cursor()

# --- DB INSERT ---
# We insert an element into the table
def saveTemperatureAndHumidity():
    now = datetime.now()
    reg_time = 0
    reg_time = now.strftime("%Y/%m/%d %H:%M:%S")
    sql = "INSERT INTO env_var_reg(reg_time, temperature, humidity) values (\'{}\', {}, {});".format(reg_time, temperature.decode(), humidity.decode())
    mycursor.execute(sql)
    print("Saving data...")
    mydb.commit()


# Connection to Telnet server (ESP module)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2)
try:
    client.connect((HOST, PORT))
except:
    print('Unable to connect')
    sys.exit()

print('Connected to remote server')
while 1:
    print("Please wait...")
    time.sleep(5)
    client.send(b'<0>')
    socket_list = [sys.stdin, client]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for sock in read_sockets:
        # incoming message from remote server
        if sock == client:
            data = sock.recv(4096)
            data.decode('utf-8')
            if not data:
                print('\nDisconnected from server')
                sys.exit()
            else:
                # print("Data received: {}".format(data))
                instruction = data.split(b';')[0]
                print(instruction)
                if instruction.decode('utf-8') == '0':
                    temperature, humidity = data.split(b';')[1:]
                    print("Temperature: {}".format(temperature))
                    print("Humidity: {}".format(humidity))
                    saveTemperatureAndHumidity()
                else:
                    print("Cannot process data: {}\n".format(data))
            # user entered a message
        # else:
        #     #msg = sys.stdin.readline()
        #     client.send('<0>')
