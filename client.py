import socket 
import os               #hacer zip a un archivo
import zipfile

def main ():
    mi_socket = socket.socket()
    mi_socket.bind( ('localhost',8000) )
    mi.socket.listen(5)
    

    with zipfile.ZipFile('Prueba.zip','r') as myzip:
    myzip.extractall()


if __name__ == "__main__":
    main()
