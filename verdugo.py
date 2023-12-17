import socket
import threading
import time

def cliente(so2,palabra,vidas):
    adivinadas = 0
    nombre = so2.recv(1024).decode()

    print(nombre+" se ha conectado.")

    so2.send(bytes(str(len(palabra)), "utf-8"))

    while adivinadas < len(palabra) and vidas > 0:
        pos = 0
        time.sleep(0.1)

        so2.send(bytes("continue", "utf-8"))
        time.sleep(0.1)

        so2.send(bytes(str(vidas),"utf-8"))

        letra = so2.recv(1024).decode()
        mantener_vidas = False

        for letr in list(palabra):
            if letr == letra:
                so2.send(str(pos).encode())

                adivinadas = adivinadas+1
                mantener_vidas = True
                time.sleep(0.1)
            pos += 1
        if not mantener_vidas:
            time.sleep(0.1)
            vidas -=  1
        so2.send(bytes("end","utf-8"))
        time.sleep(0.1)
    if vidas <= 0:
        so2.send(bytes("endgame","utf-8"))
        print(nombre+" ha perdido")
    else:
        so2.send(bytes("wingame","utf-8"))
        print(nombre+" ha ganado")
    so2.close()

palabra = input("Introduce tu palabra: ")
vidas = int(input("Introduce las vidas disponibles: "))

so = socket.socket()
so.bind(("0.0.0.0",4331))
while 1:
    so.listen()
    so2, ip = so.accept()
    hilo = threading.Thread(target=cliente,args=(so2,palabra,vidas,))

    hilo.start()
