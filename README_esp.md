# Aplicacion teoria de grafos

Script de python que encuentra la ruta mas corta entre dos estaciones del metro de santiago y la ruta con menos transbordos. Da como resultado la ruta en cuestion, la hora de salida (hora actual como programable), hora de llegada y tiempo de viaje. 

# Indice
- [Instalacion](#Instalacion)
- [Ejecucion](#Ejecucion)
- [Como usar](#Instrucciones)
- [Screenshots](#Screenshots)
  
# Instalacion 

## Requisitos

- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/)
  (python is also in microsoft store)
- pip (comes whit python)

## Linux

```bash
$ git clone https://github.com/SimuladorDeFarm/Trabajo-grafos-2024.git
$ cd Trabajo-grafos-2024
$ chmod +x install_linux_script.sh
$ ./install_linux_script.sh

```
## Windows

```cmd
$ git clone https://github.com/SimuladorDeFarm/Trabajo-grafos-2024.git
$ cd Trabajo-grafos-2024
$ install_windows_script.bat
```
O tambien puedes dirigirte a la ruta donde hayas clonado el repositorio y darle doble click al archivo `install_windows_script.bat`

# Ejecucion

Hay dos formas de ejecutar el script, usando entorno virutal (buena practica) y sin entorno virtual, en el caso de no usar entorno virtual deberas instalar manualmente las librerias listadas mas abajo en tu propia maquina

## Linux

### Entorno Virtual

```bash
#activar entorno virtual
$ source env/bin/activate
$ python main.py
#para dejar de ejecutar entorno vitual
deactivate
```
### Sin entorno virtual
Deberas instalar las librerias listadas mas abajo
```bash
$ python main.py
```
## Windows

### Entorno virtual
```cmd
#Activa entorno virual
$ call env\Scripts\activate
$ python main.py
#desacivar entorno virtual
deactivate
```
### Sin entorno virtual

instala librerias manualmente
```cmd
$ python main.py
```

### librerias usadas (se instalan automaticamente en entorno virtual)

  - [networkx](https://networkx.org/documentation/stable/install.html)
  - [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
  - [matplotlib](https://matplotlib.org/stable/users/getting_started/)
  - [tabulate](https://pypi.org/project/tabulate/)


# Instrucciones

## inputs

El programa necesita que el usuario ingrese los siguientes campos, con esos datos da como resultado la ruta mas corta y la ruta con menos transbordos.

  1) Elegir entre usar hora actual para calcular la hora de llegada o programar la hora de salida
     Desea programar hora?[si/no]: 

  si: Ingresar hora en formato hh:mm
    Programar Hora[formato HH:MM ej: 12:50]:

  no: Se usa hora actual de la maquina.

  2) Ingresar el origen y el destino, Ej:
  ingrese origen: tobalaba
  ingrese destino: macul

  4) Resultados

  Ruta mas corta: ruta mas rapida entre dos estaciones
  
  Tiempo estimado de viaje[Hrs:Min:Seg]
  Hora de salida[Hrs:Min:Seg]
  Hora de llegada[Hrs:Min:Seg]


  Ruta con menos convinaciones: ruta mas rapida entre dos estaciones
  
  Tiempo estimado de viaje[Hrs:Min:Seg]
  Hora de salida[Hrs:Min:Seg]
  Hora de llegada[Hrs:Min:Seg]

    
 
 ## Screenshots
![imagen](https://github.com/user-attachments/assets/f4915ab7-74d9-49cc-a4a1-937356625427)

# Creadores

- [SimuladorDeFarm](https://github.com/SimuladorDeFarm)
- [NeoManD10](https://github.com/NeoManD10)
- [Ari-utem](https://github.com/Ari-utem)
