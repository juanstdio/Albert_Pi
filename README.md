# Albert_Pi

Este proyecto consiste en una implementación de WolframAlpha en conjunto con OpenWeatherMap y YowSup.

* Permite resolver cálculos de hasta 2 argumentos usando el motor de WA
* Perimite saber la temperatura, humedad y presión de cualquier ciudad de la Argentina
* Permite conocer la temperatura de la CPU de la Rpi
* Se utiliza para responder pedidos a un Numero 'X' del Servicio de Whatsapp
* Posee un sistema de registro de usuarios en Archivos de texto generados por el Código.
* No realiza envíos masivos

# Comandos Disponibles:

```
Hola
```
Responde con tu nombre
```
Clima x
```
donde 'x' es cualquier cuidad de Argentina
```
Menu
```
Devuelve un listado con las opciones disponibles
```
Wa Arg1 Arg2
```
Realiza las operaciones indicadas en Arg1 y Arg2

Todo aquello que no tenga respuesta, será respondido con un mensaje de error que no se ha encontrado


### REQUISITOS:
- Raspberry Pi Model B (y posteriores, Model B+,Model 2B, Zero, Model 3)
- Una conexión a internet lo suficientemente estable vía LAN (NO recomiendo el uso de Modems 3G, ni Wi-Fi)
- Una IP fija
- Una cuenta GRATUITA en Open Weather Map
- Una cuenta en Wolfram Alpha para obtener un API_K
- Python 2.7 
```
sudo apt-get install python
```
- WolframAlpha en Python
```
pip install wolframalpha
```
- PyOWM
```
pip install pyowm
```
- Yowsup 2.7
```
pip install yowsup
```

### ¿ Como usarlo ? 

Primero deben registrar una cuenta de Whatsapp utilizando una tarjeta SIM para recibir un SMS, usando los comandos que se te detallan en la Wiki de [YowSup](https://github.com/tgalal/yowsup)
Una vez obtenido la clave, deberán adecuar el Run.py de acuerdo a sus credenciales
Luego deben modificar El [Layer.py](https://github.com/juanchip/Albert_Pi/blob/master/layer.py) para adecuarlo a las Keys generadas
por ustedes.
Finalmente, añaden el "numero" a su lista de contactos de whatsapp.

y luego ejecutan
```
python run.py
```


Agradecimientos especiales a:
* [tgalal](https://github.com/tgalal) 
* [marcoshuck](https://github.com/marcoshuck)

### Licencia

Apache License 2.0

### UTN-FRP, UNER, UTN-FRCON

