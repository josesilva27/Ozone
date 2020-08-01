import socket 
import os               #hacer zip a un archivo
import zipfile

def empaque ( path,zipActual ) :
    zipActual.write('LinkWarrior.jpg')

def main ():
    mi_socket = socket.socket()
    mi_socket.bind( ('localhost',8000) )
    mi.socket.listen(5)

    myzip = zipfile.ZipFile('Prueba.zip','w') #creo el paquete
    empaque(os.getcwd(),myzip)
    myzip.close()

    conexion,addr = mi_socket.accept()      

    while True:
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
    
if __name__ == "__main__":
    main()