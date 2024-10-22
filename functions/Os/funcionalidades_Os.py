import os

def limpiar_pantalla():
    # Si el sistema operativo es Windows, usar 'cls', en caso contrario usar 'clear'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')