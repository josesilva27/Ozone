import socket 
import os               #hacer zip a un archivo
import zipfile

def main ():
    mi_socket = socket.socket()
    mi_socket.bind( ('localhost',8000) )
    mi_socket.listen(5)
 
    
    if os.path.exists("cliente")==True:             #compruebo que existe carpeta
        ruta= os.getcwd()+"\cliente"
        if len(os.listdir(ruta))== 0:               #compruebo si esta vacia
            print("carpeta vacia")
        else:
            while True: 
                conexion,addr = mi_socket.accept()
                conexion.send("cliente conectado")

                file = open ('Prueba.zip','r')
                input_data =conexion.recv(1024)
                file.write (input_data)
                conexion.send ("archivo descargado por el cliente")
                break

        with zipfile.ZipFile('Prueba.zip','r') as myzip:        #descomprimo el archivo ZIP
            myzip.extractall()

        conexion.close()
        file.close()
        print ("El archivo se ha descargado exitosamente")
    else:
        print("Crapeta servidor no cliente, cree la carpeta y llamela 'servidor' ")

if __name__ == "__main__":
    main()
