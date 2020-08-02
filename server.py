import socket 
import os               #hacer zip a un archivo
import zipfile

def empaque ( path,zipActual ) :
    zipActual.write('LinkWarrior.jpg')

def main ():
    myzip = zipfile.ZipFile('Prueba.zip','w') #creo el paquete
    empaque(os.getcwd(),myzip)
    myzip.close()
    
    mi_socket = socket.socket()
    mi_socket.bind( ('localhost',8000) )        #creo la conexion
    mi_socket.listen(5)
     

    if os.path.exists("servidor") == True:          #compruebo que existe carpeta
        ruta= os.getcwd()+"\servidor"
        if len(os.listdir(ruta))== 0:             #compruebo si esta vacia
            print("carpeta vacia")
        else:

            while True:
                conexion,addr = mi_socket.accept() 
                print ("Nueva conexión establecida")
                print (addr)

                file = open ("Prueba.zip","rb")
                content = file.read (1024)

                while True:
                    conexion.send(content)      #envio contenido
                    content = file.read (1024)
                    conexion.send("descarga completa")
                break

            conexion.close()
            file.close()
            print ("El archivo se ha enviado exitosamente")

    else:
        print("Crapeta servidor no existe, cree la carpeta y llamela 'servidor' ")

if __name__ == "__main__":
    main()