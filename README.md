# Rock Papper Scissor / Piedra Papel Tijera

_Automata celular aplicado al juego de piedra papel o tijera._

_Este programa utiliza la [Vecindad de Moore](https://es.wikipedia.org/wiki/Vecindad_de_Moore), el color de cada píxel se calcula jugando una partida virtual de piedra, papel o tijera de 9 jugadores. La celda actual se enfrenta a sus 8 vecinos inmediatos. Si el recuento de vecinos rivales es mayoria en entonces la celda actual se convierte en la ganadora. Por ejemplo, si la celda 
actual es tijera, y el recuento de rocas es mayoria (3 o mas ya que son 8 rivales), y hay 4 rocas que la rodean, entonces se convierte en una roca._

<a href='https://github.com/Xukay101/automata-piedrapapeltijera/blob/main/gif00.gif?raw=true](https://raw.githubusercontent.com/Xukay101/automata-piedrapapeltijera/main/gif00.gif'></a>

## Instrucciones 🔧

### Pre-requisitos 📋

_Es recomendable instalar un entorno virtual para las librerias aunque no es obligatorio, para ello..._

```
$ pip install virtualenv
$ python3 -m venv env
```

_ Para instalar las librerias ejecuta:_

```
$ pip install -r requirements.txt
```

### Ejecucion 🚀

_Entra a la carpeta **rockpapperscissor** y ejecuta el archivo main_

```
$ python3 main.py
```

## Construido con 🛠️

* [PyGame](https://www.pygame.org/docs/) 
* [PyGame-Gui](https://pygame-gui.readthedocs.io/en/v_060/) 

## Autor ✒️

* **Jose Zacarías Flores**  - [Xukay101](https://github.com/Xukay101)
