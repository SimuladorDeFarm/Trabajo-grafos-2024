# Aplicacion teoria de grafos

Script de python que encuentra la ruta mas corta entre dos estaciones del metro de santiago y la ruta con menos transbordos. Da como resultado la ruta en cuestion, la hora de salida (hora actual como programable), hora de llegada y tiempo de viaje. 
![imagen](https://github.com/user-attachments/assets/f4915ab7-74d9-49cc-a4a1-937356625427)


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
```bash
$ python main.py
```


### librerias usadas (se instalan automaticamente)

  - [networkx](https://networkx.org/documentation/stable/install.html)
  - [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
  - [matplotlib](https://matplotlib.org/stable/users/getting_started/)
  - [tabulate](https://pypi.org/project/tabulate/)

