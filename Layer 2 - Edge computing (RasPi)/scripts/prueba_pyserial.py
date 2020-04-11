import serial

ser = serial.Serial('COM1', 9600)  # Abre el puerto serie con tasa de transmisi�n de 9600 baudios
print(ser.name)             # Chequea el puerto utilizado
ser.write(b'Hola gente')    # Escribe una cadena de texto en el puerto
ser.close()                 # Cierra el puerto