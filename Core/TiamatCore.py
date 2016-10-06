modulos = []
paginas = {}
RAIZ = "/Documents/PornoDuro/Tiamat/Tiamat/"
import os
HOME = os.path.expanduser("~")

#def processTemplate(ruta):
#    desgloseRuta



#def existsPage(ruta):
#    si existe la pagina en el modulo, devolver true or false, punto


def loadModules():
    f=open(HOME+RAIZ+"config", 'r')
    for linea in f:
        if linea != "":
            modulos.append(linea)

    print modulos

def loadPages(modulo):
    paginas[modulo]=[]
    f=open(HOME+RAIZ+"/"+modulo+"/config", 'r')
    for linea in f:
        if linea != "":
            paginas[modulo].append(linea)#  quitar \n

    print paginas






#TODO
#Cargar en un array global
#al inicio de la aplicacion
#el listado de modulos para
#facilitar toda esta mierda
