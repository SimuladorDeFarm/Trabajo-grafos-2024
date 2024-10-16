from datetime import datetime
import networkx as nx
#lista con lineas de metro
from functions.frontend.lista_estaciones_metro          import lista_metro



def validar_hora(hora_string):
        try:
        # Intentamos convertir la cadena a un objeto datetime con el formato "HH:MM"
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

def input_usuario():


    lista = lista_metro()
    
    #imprimir_filas(lista_estaciones)

    origen = "catolica"
    destino = "jose"
    programar_hora = True
    #obtiene la hora en formato datatime.time
    hora_string = "00:00"
    

    #en el caso de que la persna quiera programar salida
    if(programar_hora == True):
        #guarda la hora en formato string
        
        valido = True
        while valido:
            #hora_string = "15:534"
            hora_string = input("Programar Hora:")
            estacion = input("ingrese estacion: ")
            
            
            if(validar_hora(hora_string) and validar_estacion(estacion, lista)):
                valido = False
                print("Hora ingresada o estacion SI es valida")
            else:
                valido = True
                print("Hora ingresada o estacion NO es valida")
        
        #convierte la hora de string a time objet
        hora = datetime.strptime(hora_string, '%H:%M').time()
    
    #en el caso de que la persona no quiera programar salida
    else:
        #recorje la hora actual del sistema
        hora = hora_actual()

#    print(G)
#    return origen, destino, hora


