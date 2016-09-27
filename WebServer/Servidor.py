#!/usr/bin/python2.7
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PUERTO = 8888

class Controlador(BaseHTTPRequestHandler):
    def do_GET(self):
        ruta = self.path
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        #Aqui- va tu puto co-digo, Amanda
        
        
        
        
        
        
        
        #/Search?q=23123&
        if ruta == "/":
            f = open('../Core/prueba.xhtml', 'r')
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
    servidor = HTTPServer(('', PUERTO), Controlador)
    servidor.serve_forever()
except KeyboardInterrupt:
    print 'ctrl+C recibido'
    servidor.socket.close()
