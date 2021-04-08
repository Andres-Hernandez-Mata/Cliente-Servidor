"""
Uso: Servidor
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 07 Abril 2020
"""

import socket

localIP = "127.0.0.1"
localPort = 2000
bufferSize = 1024

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))
print("El servidor UDP listo para recibir preguntas del cliente")


while(True):
    recibido = UDPServerSocket.recvfrom(bufferSize)    
    mensaje = recibido[0]
    ip = recibido[1]
    print("Pregunta: " + mensaje.decode())
    print("Cliente: " + recibido[1][0])
    respuesta = input("Ingrese una respuesta: ")
    UDPServerSocket.sendto(str.encode(respuesta), ip)


