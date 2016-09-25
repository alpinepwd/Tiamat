class Peticion:
    def __init__(self, peticionRaw):
        peticion_desglose =peticionRaw.split("\n")
        self.req = peticion_desglose[0]
        self.cabeceras = {}
        for i in range(1, len(peticion_desglose)):
            entrada, valor= peticion_desglose[i].split(": ")
            self.cabeceras[entrada]= valor          
