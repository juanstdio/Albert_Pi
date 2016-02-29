# -*- Codificacion UTF-8-*-
import os, subprocess, commands #esto ya estaba, es por default de python
import pyowm        #modulo utilizado para obtener el clima
import time         #modulo para las pausas entre mensajes
import wolframalpha #modulo para el wolfram
import sys          #modulo para las operaciones a bajo nivel
import random       #modulo para los numeros aleatorios
import xlwt
from datetime import datetime

from yowsup.layers import YowLayer
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
from pyowm import OWM



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
        elif 'Wa ' in mensaje:
                id= 'XXXXXXXXXX-XXXXX' #Aca va la id que tenes de wolfram, si queres ponersela te tenes que registrar
                file = open('HistorialWA.txt', 'a')
                client = wolframalpha.Client(id)
                self.toLower(TextMessageProtocolEntity("Mathematica está calculando...", to=para))
            try:
                ParaWolfram = mensaje.split(" ")
                res = client.query(str(ParaWolfram[1]+' '+(ParaWolfram[2])))
                #Esto viene a ser un registro para saber quien fue
                # el que calculó,solo por seguridad
                file.write(str(ParaWolfram[1]+' '+(ParaWolfram[2])))
                file.write("|")
                file.write(time.strftime("%d/%m/%y"))
                file.write("|")
                file.write(time.strftime("%H:%M:%S"))
                file.write("|")
                file.write(para)
                file.write("|")
                file.write(nombre)
                file.write("\n")
                if len(res.pods) > 0:
                    texts = ""
                    pod = res.pods[1]
                if pod.text:
                    texts = pod.text
                    texts = texts.encode('ascii', 'ignore')
                    self.toLower(TextMessageProtocolEntity("Resultado:", to=para))
                    self.toLower(TextMessageProtocolEntity(texts, to=para))
                else:
                    texts = "No Tengo respuesta: Atte Don Wolfram."
                    self.toLower(TextMessageProtocolEntity(texts, to=para))
            except NameError:
                # Si me da el error de Pot
                self.toLower(TextMessageProtocolEntity("Comando Wa inválido\nError de Nombres", to=para))
            except IndexError:
                # Si Se Va de rango..(en las derivadas /integrales pasa..)
                self.toLower(TextMessageProtocolEntity("Comando Wa inválido\nindice fuera de rango", to=para))
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
