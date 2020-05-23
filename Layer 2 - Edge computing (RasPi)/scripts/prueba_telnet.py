import telnetlib

HOST = "localhost"
end = b"\r\n"

# User login data
username = b"Leandro" + end    #input("Enter your username: ")
password = b"reydemisilencio" + end    #getpass.getpass()

# Conection with server
tn = telnetlib.Telnet(HOST)
#tn.set_debuglevel(5)

# Login with username and password
tn.read_until(b"login: ")
tn.write(username)
tn.read_until(b"password: ")
tn.write(password)

##### Remote command line interface control #####

tn.read_until(b"\\Leandro>")
tn.write(b"cd Desktop" + end)

tn.read_until(b"\\Desktop>")
tn.write(b"dir" + end)

tn.read_until(b"\\Desktop>")
tn.write(b"exit" + end)

print("El contenido del escritorio es:")
print(tn.read_all().decode('ascii'))