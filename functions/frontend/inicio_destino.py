from datetime import datetime
import networkx as nx
#lista con lineas de metro
from functions.frontend.lista_estaciones_metro          import lista_metro
from functions.frontend.validaciones                    import validar_hora
from functions.frontend.validaciones                    import validar_estacion                
from functions.frontend.validaciones                    import imprimir_filas                




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


