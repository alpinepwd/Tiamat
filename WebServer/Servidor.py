#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PUERTO = 8888

class Controlador(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        f = open('../Core/prueba.xhtml', 'r')
        respuesta = ""
        for line in f:
            respuesta+=line

        self.wfile.write(respuesta)
        return
    
    def do_POST(self):
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
