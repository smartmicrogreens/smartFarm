import mysql.connector
import constants as ct

# We start the connection with the database
mydb = mysql.connector.connect(
  host = ct.HOST_DB,
  user = ct.USER_DB,
  passwd = ct.PASSWORD_DB,
  database = "db_example" # Optionally, you can choose a specific database
)

# We print a message to be sure the connection was successful
print(mydb)

# We get a reference to the database
mycursor = mydb.cursor()

############################ MANAGING DATABASES ############################

# We create a database
#mycursor.execute("CREATE DATABASE db_example")

# We show all the databases
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)

############################ MANAGING TABLES ############################

# We create a table to save data
# When creating a table, we should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.
# The statement "INT AUTO_INCREMENT PRIMARY KEY" inserts a unique number starting at 1, and increasing by one for each record.
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# We could also create the table and the modify it to add an extra column
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# We delete a table
#mycursor.execute("DROP TABLE customers")

# We delete a table if it exists
#mycursor.execute("DROP TABLE IF EXISTS customers")

# We show all the tables in the current database
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

############################ INSERTING RECORDS ############################

# We insert an element into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
#mycursor.execute(sql, val)
# We can insert multiple elements using the "executemany" method
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [ ('Ben', 'Park Lane 38'), ('William', 'Central st 954'), ('Chuck', 'Main Road 989') ]
#mycursor.executemany(sql, val)
# In order for the modification to be applied to the actual database, we must commit it
mydb.commit()

# We can obtain the amount of records in the table and the ID from the last one added
print("1 record inserted, ID:", mycursor.lastrowid)
print(mycursor.rowcount, " records inserted in total.")

############################ SELECT RECORDS ############################

# We can select which columns to select or use * to select all
#mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT name, address FROM customers")

# The method "fetchall" returns all the selected rows, while "fetchone" returns just the first one
"""
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""

############################ SELECT RECORDS WITH FILTER ############################

# We can filter the selection by using the "WHERE" statement
#mycursor.execute("SELECT * FROM customers WHERE address ='Park Lane 38'")

# When query values are provided by the user, you should escape the values to prevent SQL injections
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)

"""
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""

############################ SORTING QUERIED RECORDS ############################

# Use the ORDER BY statement to sort the result in ascending or descending order
sql = "SELECT * FROM customers ORDER BY name"       # Ascending order (default)
sql = "SELECT * FROM customers ORDER BY name DESC"  # Descending order
mycursor.execute(sql)

"""
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""

############################ DELETING RECORDS ############################

# We can delete records from an existing table by using the "DELETE FROM" statement
mycursor.execute("DELETE FROM customers WHERE address = 'Mountain 21'")
mydb.commit()

############################ UPDATING EXISTING RECORDS ############################

# We can update existing records in a table by using the "UPDATE" statement
# We can overwrite column(s) using the "SET" statement
mycursor.execute("UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'")
mydb.commit()

# Example scaping values
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()

############################ LIMITING/OFFSETTING QUERY RESULTS ############################

# We can limit the number of records returned from the query, by using the "LIMIT" statement
mycursor.execute("SELECT * FROM customers LIMIT 5") # Selects the first 5 records

# If we want to start counting from a specific record, we can use the "OFFSET" keyword
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")  # Selects the first 5 records, staring from position 3

"""
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""