import serial
import constants as ct

# Abrimos el puerto serie con tasa de transmision de 9600 baudios, sin control de paridad
ser = serial.Serial('COM1', 9600, serial.EIGHTBITS, serial.PARITY_NONE, timeout=1)
print(ser.name)             # Chequea el puerto utilizado

# Crea la cadena de bytes a enviar
# Estantería 3 - Estante 5 - Action: measure all
D = ct.ID_SHELVES + 3
E = ct.ID_SHELF_FIRST + 5
A = ct.ACT_MEASURE_ALL

instruction = bytearray([D, E, A, 0x00, 0x00, 0x00, 0x00])

ser.write(instruction)    # Escribe una cadena de texto en el puerto
print(instruction)        # Chequea el puerto utilizado

while True:
    while ser.in_waiting:  # Or: while ser.inWaiting():
        print(ser.read(7))

ser.close()               # Cierra el puerto