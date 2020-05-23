from flask import Flask # Funcionalidades básicas de Flask
from flask import render_template   # Para poder mostrar templates HTML

# Para comunicacion por Telnet
import telnetlib
# Módulo con valores constantes usados por la aplicación
import constants as const

## SÓLO PARA PRUEBAS ##
import random

app = Flask(__name__)

#################################################################
########################### Home page ###########################
#################################################################

@app.route('/')
def index():
   templateData = {
      'page' : 'index',
      'title' : 'SmartFarm - Admin'
    }
   return render_template('card_small.html', **templateData)

##################################################################
#################### Sensor measurements page ####################
##################################################################

SENSORS = { 'MEASURE_TEMP_HUM' : 'Temperatura y humedad',
            'FLIP_DEHUM' : 'Deshumidificador',
            'FLIP_LIGHT' :  'Iluminación' }

@app.route('/sensors')
def sensors():
   templateData = {
      'page' : 'sensors',
      'title' : 'Realizar medición',
      'sensors' : SENSORS
    }
   return render_template('card_small.html', **templateData)

# Individual sensor measurement
@app.route('/read/<sensor>')
def readSensor(sensor):
   nombre_sensor = sensor[1:-1]
   #unidades = { 'Temperatura' : '[°C]', 'Humedad' : '[%]', 'Caudal' : '[l/min]', 'Luminosidad' : '[lm]' }
   try:
      #### Solicitamos medición del sensor ####
      end = b"\r\n"

      # Conection with server
      tn = telnetlib.Telnet(HOST)

      # Login with username and password
      tn.read_until(b"login: ")
      tn.write(const.USERNAME_TELNET + end)
      tn.read_until(b"password: ")
      tn.write(const.PASSWORD_TELNET + end)

      ##### Remote command line interface control #####

      tn.read_until(b"ALGUNA CADENA QUE INDIQUE QUE SE PUEDE ENVIAR UN MENSAJE")
      tn.write(const.COMMANDS_TELNET[nombre_sensor] + end)

      print("El contenido del escritorio es:")
      response = tn.read_all().decode('ascii')

      tn.close()

      # Para pruebas: Temperatura aleatoria entre 15 [°C] y 35 [°C]
      #response = 'El valor medido es: ' + f"{(random.random() * 20 + 15):.2f}" + ' ' + unidades[nombre_sensor]
      #raise IOError # PARA QUE EJECUTE LA EXCEPCIÓN
   except:
      response = "Hubo un error al leer: " + SENSORS[nombre_sensor]

   templateData = {
      'page' : 'read_sensor',
      'title' : 'Respuesta',
      'response' : response
    }

   return render_template('card_small.html', **templateData)

##############################################################
#################### Database tables page ####################
##############################################################

@app.route('/tables')
def tables():
    return 'Tablas de la base datos'

################################################################
#################### Tasks programming page ####################
################################################################

@app.route('/program')
def program():
    return 'Programación de tareas'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')