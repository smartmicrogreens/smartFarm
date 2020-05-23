# Constants associated with serial communication
ID_ROBOT = 0xFE
ID_SHELVES = 0x00
ID_BROADCAST = 0xFF
ID_SHELF_FIRST = 0x00
SHELVES_COUNT = 20
ID_SHELF_LAST = ID_SHELF_FIRST + SHELVES_COUNT

# Shelving actions
ACT_WATER = 0x00
ACT_LIGHT_ON = 0x01
ACT_LIGHT_OFF = 0x02
ACT_MEASURE_TEMP = 0x03 # Air temperature
ACT_MEASURE_MOIS = 0x04 # Soil moisture
ACT_MEASURE_ALL = 0x05  # Temperature and moisture

# Robot actions
ACT_MOVE_SHELF = 0x00
ACT_INSPECT = 0x01

# Constants associated with database management
HOST_DB = "localhost"
USER_DB = "root"
PASSWORD_DB = ""
DB_NAME = "db_test"

# Constants associated with MQTT protocol
MQTT_BROKER = "localhost"