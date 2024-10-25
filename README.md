# Aplicacion teoria de grafos

Script de python que encuentra la ruta mas corta entre dos estaciones del metro de santiago y la ruta con menos transbordos. Da como resultado la ruta en cuestion, la hora de salida (hora actual como programable), hora de llegada y tiempo de viaje. 


# Instalacion 

## Requisitos

- [python](https://www.python.org/)
- pip


## Linux

```bash
$ git clone https://github.com/SimuladorDeFarm/Trabajo-grafos-2024.git
$ cd Trabajo-grafos-2024
$ chmod +x install_linux_script.sh
$ ./install_linux_script.sh

```
# Ejecucion

## Linux

### Entorno Virtual

```bash
#activar entorno virtual
$ source env/bin/activate
$ python main.py
```
### Sin entorno virtual
Deberas instalar las librerias listadas mas abajo
```bash
$ python main.py
```


### librerias usadas (se instalan automaticamente en entorno virtual)

  - [networkx](https://networkx.org/documentation/stable/install.html)
  - [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
  - [matplotlib](https://matplotlib.org/stable/users/getting_started/)
  - [tabulate](https://pypi.org/project/tabulate/)


# Como usar

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

    
 
 ## Screenshot
![imagen](https://github.com/user-attachments/assets/f4915ab7-74d9-49cc-a4a1-937356625427)

# Creadores

[SimuladorDeFarm](https://github.com/SimuladorDeFarm)
[NeoManD10](https://github.com/NeoManD10)
[Ari-utem](https://github.com/Ari-utem)
