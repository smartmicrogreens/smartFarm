
""" This instructions define the communication protocol for talking with shelf control IoT modules """

# ESP test IP address
TEST_DEVICE = '192.168.11.41'

# Read instructions
ENV_READ_STATUS = '<0>'
DEHUM_READ_STATUS = '<1>'
LIGHT_READ_STATUS = '<2>'

# Update instructions
DEHUM_UPDATE_STATUS = '<1;'
LIGHT_UPDATE_STATUS = '<2;'

# Character of End Of Line
EOL = '>'

# Status options
ON = True
OFF = False

# Shelfs
SHELF_1 = 0
SHELF_2 = 1
SHELF_3 = 2
SHELF_4 = 3
