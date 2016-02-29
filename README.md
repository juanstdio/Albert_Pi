# Albert_Pi

Este proyecto consiste en una implementación de WolframAlpha en conjunto con OpenWeatherMap y YowSup.

* Permite resolver cálculos de hasta 2 argumentos usando el motor de WA
* Perimite saber la temperatura, humedad y presión de cualquier ciudad de la Argentina
* Permite conocer la temperatura de la CPU de la Raspberry Pi

Se utiliza para responder pedidos a un Numero 'X' del Servicio de Whatsapp.

### REQUISITOS:
- Raspberry Pi Model B (y posteriores, Model B+,Model 2B, Zero, Model 3)
- Una conexión a internet lo suficientemente estable vía LAN (NO recomiendo el uso de Modems 3G, ni Wi-Fi)
- Una IP fija
- Una cuenta GRATUITA en Open Weather Map para obtener una Key
- Una cuenta en Wolfram Alpha para obtener un API_K
 

- Python 2.7 -> 
```
sudo apt-get install python
```
- WolframAlpha_API ->
```
pip install wolframalpha
```
- PyOWM -> 
```
pip install pyowm
```
-Yowsup 2.7 -> 
```
pip install yowsup
```

### ¿ Como usarlo ? 

Primero deben registrar una cuenta de Whatsapp utilizando una tarjeta SIM para recibir un SMS, usando los comandos que se te detallan en la Wiki de YowSup.
Una vez obtenido la clave, deberán adecuar el Run.py de acuerdo a sus credenciales
Luego deben modificar El [Layer.py](https://github.com/juanchip/Albert_Pi/blob/master/layer.py) para adecuarlo a las Keys generadas
por ustedes.

Luego es cuestión de añadir el contacto a su app de whatsapp y listo!

### Licencia

Apache License 2.0

### UTN-FRP, UNER, UTN-FRCON

