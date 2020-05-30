# Constants associated with database management
HOST_DB = "localhost"
USER_DB = "root"
PASSWORD_DB = ""
DB_NAME = "db_test"

# Constants for connection with Telnet server
HOST_TELNET = "localhost"
USERNAME_TELNET = b"testing"
PASSWORD_TELNET = b"1234567890"

# Commands for communication with Telnet server
ACT_MEASURE_TEMP_HUM = '0'  # Measure air temperature and humidity
ACT_FLIP_DEHUM = '1'        # Flip state of dehumidifier (on/off)
ACT_FLIP_LIGHT = '2'        # Flip state of lights (on/off)
########### IDEAS PARA COMANDOS ###########
ACT_FLIP_WATER = '3'        # Flip state of water pump (on/off)
ACT_MEASURE_MOIS = '4'      # Measure soil moisture
ACT_MEASURE_TEMP = '5'      # Measure air temperature
ACT_MEASURE_HUM = '6'       # Measure air humidity
ACT_DEHUM_ON = '7'          # Turn on dehumifier
ACT_DEHUM_OFF = '8'         # Turn off dehumifier
ACT_LIGHT_ON = '9'          # Turn on light
ACT_LIGHT_OFF = '10'        # Turn off light
ACT_WATER_ON = '11'         # Turn on water pump
ACT_WATER_OFF = '12'        # Turn off water pump
ACT_SET_WATER = '13'        # Set water pump flow -> Command: ACT_SET_WATER + FLOW_LEVEL

# Lo mismo reimplementado como diccionario, más cómodo :p
COMMANDS_TELNET = {
    'MEASURE_TEMP_HUM' : '0',  # Measure air temperature and humidity
    'FLIP_DEHUM' : '1',        # Flip state of dehumidifier (on/off)
    'FLIP_LIGHT' : '2',        # Flip state of lights (on/off)
    ########### IDEAS PARA COMANDOS ###########
    'FLIP_WATER' : '3',        # Flip state of water pump (on/off)
    'MEASURE_MOIS' : '4',      # Measure soil moisture
    'MEASURE_TEMP' : '5',      # Measure air temperature
    'MEASURE_HUM' : '6',       # Measure air humidity
    'DEHUM_ON' : '7',          # Turn on dehumifier
    'DEHUM_OFF' : '8',         # Turn off dehumifier
    'LIGHT_ON' : '9',          # Turn on light
    'LIGHT_OFF' : '10',        # Turn off light
    'WATER_ON' : '11',         # Turn on water pump
    'WATER_OFF' : '12',        # Turn off water pump
    'SET_WATER' : '13'         # Set water pump flow -> Command: ACT_SET_WATER + FLOW_LEVEL
}