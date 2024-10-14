from datetime import datetime

def hora_actual():

    hora= datetime.now().time()

    return hora



def input():

    origen = ""
    destino = ""

    #obtiene la hora en formato datatime.time
    hora = hora_actual()

    return origen, destino, hora


origen, destino, hora = input()

