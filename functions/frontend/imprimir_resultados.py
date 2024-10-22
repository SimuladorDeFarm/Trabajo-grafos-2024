from tabulate import tabulate
from functions.base_datos.combinaciones import combinaciones

#imprime la ruta que hay que tomar, esta contenida en el el array 1dimension ruta
#v es un vector que contiene las convinaciones del metro para que cuando
#se haga una convinacion se imrpima en que estacion convinar pero la funcion fue eliminada por problemas con la rtua de menor duracion 

def eliminar_repetidos(lista):
    seen = set()  # Para rastrear elementos que ya hemos visto
    resultado = []  # Lista resultado sin el segundo repetido

    for elemento in lista:
        if elemento not in seen:
            seen.add(elemento)
            resultado.append(elemento)
        elif lista.count(elemento) > 1:
            # Si ya apareció una vez, no lo agregamos
            seen.add(elemento)
    return resultado




def imprimir_tabulate(ruta, v):

    ruta = eliminar_repetidos(ruta)

    # Crear una tabla con las líneas de metro
    tabla = [[i+1, linea] for i, linea in enumerate(ruta)]
    
    print(tabulate(tabla, headers=["Paso", "Línea de Metro"]))
    
    '''
    #obtiene el largo del aray 1d de ruta y de v
    lar_ruta = len(ruta)
    lar_v    = len(v)
    
    #variable que guarda si se hace o no una convinacion
    combinacion = False

    #indices para recorrer el ciclo anidado
    i = 0
    j = 0
    
    #while anidado que busca las estaciones de la ruta que tambien estan en el
    #array v que contiene que estaciones son combinaciones, si es que se 
    #la estacion es convinacion entonces: combinacion = True e imprimira ---> combinacion
    
    #recorre la lista con la ruta
    while i <   lar_ruta:
        j = 0
        #se recetea conbinacion para el siguiente ciclo
        combinacion = False
        #recorre la lista con las convinaciones
        while j < lar_v:
            
            #si es que la estacion de la ruta es una combinacion
            if ruta[i] == v[j]:
                combinacion = True
            j+=1

        if combinacion == True:
            print( i+1, "|", ruta[i], "---> Combinacion" )
        else:
            print( i+1, "|", ruta[i] )

        i+=1
        '''

'''
imprimir ruta con menos transbordos imprime todos los campos de la ruta corta:
    partida,
    destino
    tiempo de viaje
    hora de salida
    hora de llegda
    recorrido estaciones
''' 
def imprimir_ruta_menos_transbordos(origen , destino, camino, transbordos, estaciones_transbordo, tiempo_recorrido, hora_llegada, hora_salida ):

    #v = combinaciones()
    #desactivo lesta funcion de mostrar donde estan als convinaciones porque no pude aplicarlo a rutas mas cortas
    v = [0]
    print("-------------------------")
    if camino:
        print(f"La ruta con menor cantidad de transbordos entre {origen} y {destino} es:")
        print( "Tiempo estimado de viaje[Hrs:Min:Seg]: ",tiempo_recorrido)
        print("Hora de salida[Hrs:Min:Seg]: ", hora_salida)
        print("Hora de llegada[Hrs:Min:Seg]: ", hora_llegada.time())
        imprimir_tabulate(camino, v)
        #print(" -> ".join(camino))
        print(f"Número total de transbordos realizados: {transbordos}")
        if estaciones_transbordo:
            print(f"Transbordos realizados en las siguientes estaciones: {', '.join(estaciones_transbordo)}")
        else:
            print("No se realizaron transbordos.")
    else:
        print("No se encontró una ruta.")



'''
imprimir ruta corta imprime todos lso campos de la ruta corta:
    partida,
    destino
    tiempo de viaje
    hora de salida
    hora de llegda
    recorrido estaciones
''' 
#ruta = array 1d  contiene la ruta con menos convinaciones: 
#hora_llegada = datatime.datatime
#tiempo_recorrido: datatime.time
#origen: string
#destino: string
#hora:salida: datatime.time
def imprimir_ruta_corta(ruta, hora_llegada, tiempo_recorrido, origen, destino, hora_salida):
    #v = combinaciones()

    print( "Partida:  ", origen)
    print( "Destino:  ", destino)
    print( "Tiempo estimado de viaje[Hrs:Min:Seg]: ",tiempo_recorrido)
    print("Hora de salida[Hrs:Min:Seg]: ", hora_salida)
    print("Hora de llegada[Hrs:Min:Seg]: ", hora_llegada.time())

    v = [0]
    #print("ruta de viaje: ", ruta)
    imprimir_tabulate(ruta, v )