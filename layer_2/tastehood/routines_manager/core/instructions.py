
""" This instructions define the communication protocol for talking with shelf control IoT modules """

# Read instructions
ENV_READ_STATUS = b'<0>'
DEHUM_READ_STATUS = b'<1>'
LIGHT_READ_STATUS = b'<2>'

# Update instructions
LIGHT_UPDATE_STATUS = '<2;'
DEHUM_UPDATE_STATUS = '<3;'

# Character of End Of Line
EOL = '>'
