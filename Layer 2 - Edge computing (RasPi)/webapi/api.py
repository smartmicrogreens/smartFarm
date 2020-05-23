from flask import Flask # Funcionalidades básicas de Flask
from flask import render_template   # Para poder mostrar templates HTML

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

@app.route('/sensors')
def sensors():
   templateData = {
      'page' : 'sensors',
      'title' : 'Realizar medición'
    }
   return render_template('card_small.html', **templateData)

# Individual sensor measurement
@app.route('/read/<sensor>')
def readSensor(sensor):
   nombre_sensor = sensor[1:-1]
   unidades = { 'temperatura' : '[°C]', 'humedad' : '[%]', 'caudal' : '[l/min]' }
   try:
      #### AGREGAR MEDICIÓN DEL SENSOR ####

      # Para pruebas: Temperatura aleatoria entre 15 [°C] y 35 [°C]
      response = 'El valor medido es: ' + f"{(random.random() * 20 + 15):.2f}" + ' ' + unidades[nombre_sensor]
      #raise IOError # PARA QUE EJECUTE LA EXCEPCIÓN
   except:
      response = "Hubo un error al leer el sensor de " + nombre_sensor

   templateData = {
      'page' : 'read_sensor',
      'title' : 'Valor medido por el sensor de ' + nombre_sensor,
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