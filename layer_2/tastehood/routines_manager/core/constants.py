
""" This instructions define the communication protocol for talking with shelf control IoT modules """

# ESP test IP address
TEST_DEVICE = '192.168.11.41'

# Read instructions
ENV_READ_STATUS = '<0>'
HUMID_READ_STATUS = '<1>'
LIGHT_READ_STATUS = '<2>'
TEMP_READ_STATUS = '<3>'
WATER_READ_STATUS = '<4>'

# Update instructions
HUMID_UPDATE_STATUS = '<1;'
LIGHT_UPDATE_STATUS = '<2;'
TEMP_UPDATE_STATUS = '<3;'
WATER_UPDATE_STATUS = '<4;'

# Character of End Of Line
EOL = '>'

# Read/update tuples
LIGHT = (LIGHT_READ_STATUS, LIGHT_UPDATE_STATUS)
HUMID = (HUMID_READ_STATUS, HUMID_UPDATE_STATUS)
TEMP = (TEMP_READ_STATUS, TEMP_UPDATE_STATUS)
WATER = (WATER_READ_STATUS, WATER_UPDATE_STATUS)

# Status options
ON = True
OFF = False

# Shelfs
SHELF_1 = 0
SHELF_2 = 1
SHELF_3 = 2
SHELF_4 = 3
