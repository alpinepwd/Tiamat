modulos = []
paginas = {}
RAIZ = "/Documents/PornoDuro/Tiamat/Tiamat/"
import sys

import os
HOME = os.path.expanduser("~")

def processTemplate(ruta):
    print "PT: "
    print ruta
    print "pag: "+ruta.pagina
    pm = get_class(ruta)
    controlador = pm()


##Parser XHTMl
##Cargar todo el texto y substituir los {}
##ejecutar el .py desde ahi y (??)

#    desgloseRuta



def existsPage(ruta):
    print ruta
    print paginas
    if ruta.pagina in paginas[ruta.modulo]:
        print "existsPage"
        return True
    else:
        print "NO!!"
        return False

##si existe la pagina en el modulo, devolver true or false, punto
#    for modulo in modulos:
#        if ruta.startswith("/"+modulo+"/"):
#            for pagina in paginas[modulo]:
#                if "/"+pagina == ruta:
#                    return True
#    return False




def loadModules():
    print "loadModules: "
    f=open(HOME+RAIZ+"config", 'r')
    for linea in f:
        if linea != "":
            modulos.append(linea.strip())
            sys.path.insert(0, HOME+RAIZ+linea.strip()+"/businessObjects")
            sys.path.insert(0, HOME+RAIZ+linea.strip()+"/pageManagers")
            sys.path.insert(0, HOME+RAIZ+linea.strip())

    print sys.path
    print modulos

def loadPages(modulo):
    print "loadPages: "+modulo
    paginas[modulo]=[]
    f=open(HOME+RAIZ+"/"+modulo+"/config", 'r')
    for linea in f:
        if linea != "":
            paginas[modulo].append(linea.strip())#  quitar \n

    print paginas



def get_class(kls):
    print "kls: "
    print kls
    #parts = kls.split('.')
    #module = ".".join(parts[:-1])
    #print module+"\n\n\n"
    print kls.modulo
    print kls.pagina
    m = __import__(kls.modulo+".pageManager."+kls.pagina)
    
    m=getattr(m, "pageManager")
    m=getattr(m, kls.pagina)
    m=getattr(m, kls.pagina)
    #m2 = __import__(pageManagers)
    #+".pageManager."+kls.pagina)
#    for comp in parts[1:]:
#        m = getattr(m, comp)
    return m


#TODO
#Cargar en un array global
#al inicio de la aplicacion
#el listado de modulos para
#facilitar toda esta mierda
