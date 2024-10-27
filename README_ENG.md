# Graph Theory Application

Python script that find the quickest rute and rute whit least transfer between two subway station.  The program gives us two rutes, departure time(current hour or programmed) , arrive time and travel time.

# Index
- [Installation](#Installation)
- [Execution](#Execution)
- [Como usar](#Instrucciones)
- [Screenshots](#Screenshots)
  
# Installation 

## Requirements

- [python](https://www.python.org/)
- pip


## Linux

Clone the repositoy and execute the script `install_linux_script.sh`.
```bash
$ git clone https://github.com/SimuladorDeFarm/Trabajo-grafos-2024.git
$ cd Trabajo-grafos-2024
#change permissions
$ chmod +x install_linux_script.sh
$ ./install_linux_script.sh

```
## Windows

Clone the repositoy and execute the script `install_windows_script.bat`.
```cmd
$ git clone https://github.com/SimuladorDeFarm/Trabajo-grafos-2024.git
$ cd Trabajo-grafos-2024
$ install_windows_script.bat
```
Or you can also go to the path where you have cloned the repository and double-click in the file `install_windows_script.bat` 


# Execution

There are two ways to execute this script: using a virtual environment (good practice) and without a virtual environment. If you choose not to use a virtual environment, you will need to manually install the libraries listed below on your own machine.

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
