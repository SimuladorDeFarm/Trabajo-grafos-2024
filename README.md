# Graph Theory Application

Python script that find the quickest rute and rute whit least transfer between two subway station.  The program gives us two rutes, departure time(current hour or programmed) , arrive time and travel time.

# Index
- [Installation](#Installation)
- [Execution](#Execution)
- [Como usar](#Instructions)
- [Screenshots](#Screenshots)
- [Creators](#Creators)  
# Installation 

## Requirements

- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/)
  (python is also in microsoft store)
- pip (comes whit python)


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

### Virtual Enviroment 

```bash
#activar entorno virtual
$ source env/bin/activate
$ python main.py
#para dejar de ejecutar entorno vitual
deactivate
```
### Without Virtual Enviroment

Install the libraries listed bellow
```bash
$ python main.py
```
## Windows

### Virtual Enviroment
```cmd
#Activa entorno virual
$ call env\Scripts\activate
$ python main.py
#desacivar entorno virtual
deactivate
```
### without  Virtual Enviroment

Install the libraries listed bellow
```cmd
$ python main.py
```

### libraries used 

  - [networkx](https://networkx.org/documentation/stable/install.html)
  - [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
  - [matplotlib](https://matplotlib.org/stable/users/getting_started/)
  - [tabulate](https://pypi.org/project/tabulate/)


# Instructions

To obtain de quickest rute and the route with the least transfers you need put departure time, origin and destination

  

  1) Choouse between the current time or programming time:
    `Desea programar hora?[si/no]:` 

  si: Get into time in format hh:mm :
    Programar Hora[formato HH:MM ej: 12:50]:

  no: use current time.

  2) Get into origin and destiny, Ej:
  ingrese origen: tobalaba
  ingrese destino: macul

  4) Result

  quickest rute: 
  
  Tiempo estimado de viaje[Hrs:Min:Seg]
  Hora de salida[Hrs:Min:Seg]
  Hora de llegada[Hrs:Min:Seg]


  rute whith least transfers: 
  
  Tiempo estimado de viaje[Hrs:Min:Seg]
  Hora de salida[Hrs:Min:Seg]
  Hora de llegada[Hrs:Min:Seg]

    
 
 ## Screenshots
![imagen](https://github.com/user-attachments/assets/f4915ab7-74d9-49cc-a4a1-937356625427)

# Creators

- [SimuladorDeFarm](https://github.com/SimuladorDeFarm)
- [NeoManD10](https://github.com/NeoManD10)
- [Ari-utem](https://github.com/Ari-utem)
