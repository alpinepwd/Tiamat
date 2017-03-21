import string


class Ruta(object):
    "Clase que representa una ruta, consistente en modulo + pagina + argumentos"
    def __init__(self, ruta_completa):
        "Constructor de ruta"
        ruta_array = string.split(ruta_completa,"?")
        print "rutaCompleta: "+ruta_completa
        self.parametros = {}
        if len(ruta_array) == 0:
            #TODO aqui falta ver que pasa
            return
        elif len(ruta_array) == 1:
            self.ruta = ruta_completa
        else:
            self.ruta = ruta_array[0]
            parametros_array = string.split(ruta_array[1],"&")
            for par in parametros_array:
                par_div = string.split(par, "=")
                
                if len(par_div) == 1:
                    self.parametros[par_div[0]] = ""
                else:
                    self.parametros[par_div[0]] = par_div[1]

        aux_ruta_arr = string.split(self.ruta, "/")
        self.modulo = aux_ruta_arr[1]
        self.pagina = "/".join(aux_ruta_arr[2:])

    def __str__(self):
        return self.modulo+"/"+self.pagina
