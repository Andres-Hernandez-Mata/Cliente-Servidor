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

UPDClienteSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

