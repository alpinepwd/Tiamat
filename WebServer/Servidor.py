#!/usr/bin/python2.7

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import string
import re
import os
RAIZ = "/Documents/PornoDuro/Tiamat/Tiamat/"
HOME = os.path.expanduser("~")

import sys
sys.path.insert(0, HOME+RAIZ+'Core')
import TiamatCore


PUERTO = 8888

class Controlador(BaseHTTPRequestHandler):
    def do_GET(self):
        ruta_completa = self.path
#        self.send_response(200)
#        self.send_header('Content-type', 'text/html')
#        self.end_headers()
        ruta_array = string.split(ruta_completa,"?")
        print ruta_completa
        parametros = {}
        if len(ruta_array) == 0:
            #TODO aqui falta ver que pasa
            return
        elif len(ruta_array) == 1:
            ruta = self.path
        else:
            ruta = ruta_array[0]
            parametros_array = string.split(ruta_array[1],"&")
            for par in parametros_array:
                par_div = string.split(par, "=")
                
                if len(par_div) == 1:
                    parametros[par_div[0]] = ""
                else:
                    parametros[par_div[0]] = par_div[1]


        print ruta
        if ruta.endswith(".css"):
            try:
                archivo = open(HOME+RAIZ+ruta, 'r')
                respuesta=""
                for line in archivo:
                    respuesta += line
            
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(respuesta)
                return
            except IOError:
                self.send_response(404)
                self.end_headers()
                return

        if ruta.endswith(".gif"):
            try:
                archivo = open(HOME+RAIZ+ruta, 'rb')
                respuesta=""
                for line in archivo:
                    respuesta += line
        
                self.send_response(200)
                self.send_header('Content-type', 'image/gif')
                self.end_headers()
                self.wfile.write(respuesta)
                return
            except IOError:
                self.send_response(404)
                self.end_headers()
                return

        if ruta.endswith(".jpg"):
            try:
                archivo = open(HOME+RAIZ+ruta, 'rb')
                respuesta=""
                for line in archivo:
                    respuesta += line
            
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(respuesta)
                return
            except IOError:
                self.send_response(404)
                self.end_headers()
                return



        if ruta.endswith(".js"):
            try:
                archivo = open(HOME+RAIZ+ruta, 'rb')
                respuesta=""
                for line in archivo:
                    respuesta += line
            
                self.send_response(200)
                self.send_header('Content-type', 'application/x-javascript')
                self.end_headers()
                self.wfile.write(respuesta)
                return
            except IOError:
                self.send_response(404)
                self.end_headers()
                return
    #
    #        p = re.compile('\.tiff$')
    #        if p.match(ruta) != None:
    #            return
    #

        if ruta.statswith("/Core/"):
            if(TiamatCore.existsPage(ruta)):
                respuesta = TiamatCore.processTemplate(ruta)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(respuesta)
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

    

        if ruta == "/":
            f = open(HOME+RAIZ+'Core/prueba.xhtml', 'r')
            respuesta = ""
            for line in f:
                respuesta += line
        else:
            respuesta="yuju"

        self.wfile.write(respuesta)
        return

    def do_POST(self):
        ruta = self.path
        if ruta != "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Hey, funciona")
        return
    
    
try:
#    cargar Core
#    cargar resto de modulos
    TiamatCore.loadPages('Core')
    print "Iniciando servidor"
    servidor = HTTPServer(('', PUERTO), Controlador)
    servidor.serve_forever()
except KeyboardInterrupt:
    print 'ctrl+C recibido'
    servidor.socket.close()
