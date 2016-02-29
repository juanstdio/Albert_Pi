# -*- Codificacion UTF-8-*-
import os, subprocess, commands #esto ya estaba, es por default de python
import RPi.GPIO as GPIO
import pyowm        #modulo utilizado para obtener el clima
import time         #modulo para las pausas entre mensajes
import wolframalpha #modulo para el wolfram
import sys          #modulo para las operaciones a bajo nivel
import random       #modulo para los numeros aleatorios
import xlwt
from datetime import datetime



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

from yowsup.layers import YowLayer
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity

from pyowm import OWM
import funciones


class EchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print "ack: ", entity.ack()
        self.toLower(entity.ack())

    def onTextMessage(self, messageProtocolEntity):

        nombre = messageProtocolEntity.getNotify()
        mensaje = messageProtocolEntity.getBody()
        para = messageProtocolEntity.getFrom()

        print 'Esta hablando: ' + nombre


        archivo = open('RegistroDeUsuarios.txt', 'a')
        archivo.write(time.strftime("%d/%m/%y"))
        archivo.write("|")
        archivo.write(time.strftime("%H:%M:%S"))
        archivo.write("|")
        archivo.write(para)
        archivo.write("|")
        archivo.write(nombre)
        archivo.write("\n")
        archivo.close() # Fin de registro de usuarios
        if mensaje == 'Hola':

            msg1 = "Hola " + nombre + " como estas ?"


            self.toLower(TextMessageProtocolEntity(msg1, to=para))
        elif 'Clima' in mensaje:
                ParaClima = mensaje.split(' ')

                owm_es = OWM(language='es')
                Pais = ',Arg'
                API_key = '12345678'
                owm = OWM(API_key)
                apikey = owm.get_API_key()

                owm.set_API_key(API_key)
                observation = owm.weather_at_place(ParaClima[1] + Pais)
                w = observation.get_weather()
                presion = str(w.get_pressure())


                presionseparada = presion.split(':')
                presA = presionseparada[1]
                PresF = presA.split(',')

                time.sleep(1)
                temperatura = str(w.get_temperature('celsius'))

                temperaturaSeparada = temperatura.split(':')
                TempA = temperaturaSeparada[3]
                TempF = TempA.split(',')
                humedad = w.get_humidity()
                self.toLower(TextMessageProtocolEntity('Presion: ' + PresF[0] + ' hPa\n''Temperatura: ' + TempF[0] + '[C]\n'+ 'Humedad: ' + str(humedad) + ' %' , to=para))
                time.sleep(1)


                os.system("twitter set Me ha consultado " + nombre + "...")
                time.sleep(1)
        elif mensaje == 'Gracias':
            msg10 = "Estoy siendo programado, teneme paciencia"
            time.sleep(1)
            msg11 = "Para mas informacion, escribe Menu"
            time.sleep(2)
            self.toLower(TextMessageProtocolEntity(msg10, to=para))
            time.sleep(1)
            self.toLower(TextMessageProtocolEntity(msg11, to=para))

        elif mensaje == 'Menu':
            msg12 = "Bievenido " + nombre
            msg12 += "\n1) Te digo el clima (Clima + Ciudad.. Ej: Clima Concordia). "
            msg12 += "\n2) Imagenes de camara area (en desarrollo). "
            msg12 += "\n3) Altura del rio Uruguay (Puerto + Nomb. Ciudad) Ej: 'Puerto Concordia'. \n Para saber todos los puertos disponibles escriba 'Puertos'. "
            msg12 += "\nDesarrollado por Franco Ruis Dias (UNER), Dual Giupponi (UTNFRCON) y Juan Blanc (UTNFRP)."

            self.toLower(TextMessageProtocolEntity(msg12, to=para))
            time.sleep(1)
        elif mensaje == 'Temp':
            temp = open("/sys/class/thermal/thermal_zone0/temp")
            cpu_temp = temp.read()
            temp.close()
            t = float(cpu_temp) / 1000
            enviar = "Tempertura CPU: " + str(t)
            self.toLower(TextMessageProtocolEntity(enviar, to=para))
        else:
            msg104 = "Palabra no reconocida por el servidor. Para mas opciones, envie un mensje con la palabra 'menu'"
            time.sleep(1)
            self.toLower(TextMessageProtocolEntity(msg104, to=para))
