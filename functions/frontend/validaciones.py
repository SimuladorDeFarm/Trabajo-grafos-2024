from datetime import datetime


def validar_hora(hora_str):

    hora = hora_str.split(":")

    hora[0] = int(hora[0])
    hora[1] = int(hora[1])
    
    if hora[0] >= 0 and hora[0] < 25:
        print("Hora es correcota")
    else:
        #print("Hora es incorrecota")
        return False

    if hora[1] >= 0 and hora[1] < 60:
        print("Min es correcota")
    else:
        return False 

    return True


#valida la hora para el formato Hora y minutos
def validar_hora(hora_string):
        try:
        # convertir la cadena a un objeto datetime con el formato "HH:MM"
            datetime.strptime(hora_string, "%H:%M")
            return True  # Si no ocurre excepción, el formato es correcto
        except ValueError:
            return False  # Si hay una excepción, el formato no es válido

def validar_estacion(estacion_usr, lista_estaciones):
    
    existe = False

    n = len(lista_estaciones) -1
    for i in range(n):

        if estacion_usr == lista_estaciones[i][0]:
            existe = True
    for j in range(n):

        if estacion_usr == lista_estaciones[j][1]:
            existe = True


    return existe

def imprimir_filas(lista):
        
        n = len(lista)
        for i in range(n-1):
            print(lista[i][0])

