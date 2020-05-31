import socket
import sys, select, string
import mysql.connector
import time

# MySQL configuration information
mydb = mysql.connector.connect(
    host='localhost',
    user='microgadmin',
    passwd='Hostname.123',
    database="microg"
)

mycursor = mydb.cursor()

############################ MANAGING TABLES ############################

# We create a table to save data
# When creating a table, we should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.
# The statement "INT AUTO_INCREMENT PRIMARY KEY" inserts a unique number starting at 1, and increasing by one for each record.

envVarReg = mycursor.execute("CREATE TABLE env_var_reg (reg_time TIME, temperature FLOAT, humidity FLOAT)")
mycursor.execute("CREATE TABLE env_var_reg (id INT AUTO_INCREMENT PRIMARY KEY, reg_time TIME, temperature FLOAT, humidity FLOAT)")