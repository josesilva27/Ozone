import os               #hacer zip a un archivo
import zipfile
"""
def empaque ( path,zipActual ) :
    zipActual.write('LinkWarrior.jpg')

if __name__ == "__main__":
    myzip = zipfile.ZipFile('Prueba.zip','w') #abro el paquete
    empaque(os.getcwd(),myzip)
    myzip.close()
 
print( "finalizado" )
"""

# descomprimir un archivo

with zipfile.ZipFile('Prueba.zip','r') as myzip:
    myzip.extractall()

print ("finalizado!")
