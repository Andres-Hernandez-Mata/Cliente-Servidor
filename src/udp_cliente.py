"""
Uso: Cliente
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 07 Abril 2020
"""

import socket
import sys

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    pregunta = input("Ingrese una pregunta: ")
    if pregunta == "bye":
        UDPClientSocket.close()
        sys.exit()
    else:
        UDPClientSocket.sendto(str.encode(pregunta), servidor)
        mensaje = UDPClientSocket.recvfrom(bufferSize)
        respuesta = "Respuesta: " + mensaje[0].decode()
        print(respuesta)

