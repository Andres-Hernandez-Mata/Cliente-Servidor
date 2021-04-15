"""
Uso: Cliente
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

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

banner = header.figlet_format("CLIENTE UDP").upper()
print(colored(banner.rstrip("\n"), 'yellow', attrs=['bold']))

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        pregunta = input("Ingrese una pregunta: ")
        if pregunta == "bye":
            UDPClientSocket.sendto(str.encode(pregunta), servidor)
            UDPClientSocket.close()
            print("Saliendo...")
            sys.exit()
        else:
            UDPClientSocket.sendto(str.encode(pregunta), servidor)
            mensaje = UDPClientSocket.recvfrom(bufferSize)
            respuesta = "Respuesta: " + mensaje[0].decode()
            print(respuesta)
except Exception:
    print(Fore.RED + "Ocurrio una excepción en la conexion del servidor" + Style.RESET_ALL)
