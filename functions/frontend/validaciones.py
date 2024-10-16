
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


