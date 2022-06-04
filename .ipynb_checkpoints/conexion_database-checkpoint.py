import sys
import socket
import mariadb
from sqlalchemy import create_engine

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)   

try:
    #Laptop Tandamos
    sys.path.insert(1, "C:/Users/franc/Desktop")
    import mariadb_creds
    
except ModuleNotFoundError:
    print('No Laptop Tandamos')

else:
    print('Laptop Tandamos')

    
try: 
    # SpartanPC
    sys.path.insert(1, "C:/Users/franpc/Desktop")
    import mariadb_creds
    
except ModuleNotFoundError:
    print('No SpartanPC')

else:
    print('Spartan PC')
    

# Obtener credenciales de otro archivo
user = mariadb_creds.user
password = mariadb_creds.password
host = mariadb_creds.host
database = mariadb_creds.database

# Crear conexión con la base de datos
c_connection = 'mariadb+mariadbconnector://{0}:{1}@{2}:3306/{3}'
c_connection = c_connection.format(user, password, host, database)
engine = create_engine(c_connection)