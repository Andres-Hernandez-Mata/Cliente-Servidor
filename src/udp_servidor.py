"""
Uso: Servidor
Creado: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 07 Abril 2020
"""

import socket
import sys
import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored

os.system("cls")

localIP = "127.0.0.1"
localPort = 2000
bufferSize = 1024

banner = header.figlet_format("SERVIDOR UDP").upper()
print(colored(banner.rstrip("\n"), 'yellow', attrs=['bold']))

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("El servidor UDP listo para recibir preguntas del cliente")

try:
    while True:
        recibido = UDPServerSocket.recvfrom(bufferSize)    
        mensaje = recibido[0]
        mensaje = mensaje.decode()
        if mensaje == "bye":
            UDPServerSocket.close()
            sys.exit()
        else:
            ip = recibido[1]
            cliente = recibido[1][0]
            print("Pregunta: " + mensaje)
            print("Cliente: " + cliente)
            respuesta = input("Ingrese una respuesta: ")
            UDPServerSocket.sendto(str.encode(respuesta), ip)
except Exception:
    print(Fore.RED + "Ocurrio una excepción en la conexion del cliente" + Style.RESET_ALL)

