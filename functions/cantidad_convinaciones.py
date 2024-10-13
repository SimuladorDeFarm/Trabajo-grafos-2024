
def cantidad_convinaciones(rutas, convinaciones):

    n_filas = len(rutas)
    n_columnas = len(rutas[0])
    
    #numero de filas de las convinaciones
    n_filas_c = len(convinaciones)

    #contar cantidad de convinaciones
    contador = [0] * n_filas

    i = 0
    j = 0
    x = 0
    
    while i < n_filas:
        n_columnas = len(rutas[i])
        j = 0
        while j < n_columnas:
            x = 0
            

            while x < n_filas_c:

                if convinaciones[x] == rutas[i][j] :
                    
                    #cuenta la catidad de convinaciones
                    contador[i]+=1
                x+=1
            j+=1
        i+=1
    #ordena el arreglo de menor  a mayor
    contador.sort()
    
    return contador[0]
    