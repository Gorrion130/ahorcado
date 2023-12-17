import socket
import os

so = socket.socket()

nombre = input("Introduce tu nombre: ")
ip = input("Introduce la ip del server: ")

so.connect((ip, 4331))
so.send(bytes(nombre,"utf-8"))

letras = so.recv(1024).decode()
ahorcado = "_"*int(letras)
letrasEscritas = []

while 1:
    datos = so.recv(1024).decode()
    if datos != "endgame":
        if datos == "wingame":
            os.system("clear")

            print(ahorcado)
            print("\nVidas: "+str(vidas))
            print("\nLetras: "+str(letrasEscritas))
            print("Has ganado :)")
            
            break
        os.system("clear")

        print(ahorcado)
        
        vidas = so.recv(1024).decode()
        
        print("\nVidas: "+str(vidas))
        print("\nLetras usadas: "+str(letrasEscritas))
        
        letra = input("\n\n\nIntroduce una letra: ")
        while letra in letrasEscritas or len(letra) != 1:
            os.system("clear")
            
            print(ahorcado)
            print("\nVidas: "+str(vidas))
            print("\nLetras usadas: "+str(letrasEscritas))
            
            letra = input("\n\n\nIntroduce una letra: ")
        so.send(bytes(letra,"utf-8"))
        letrasEscritas.append(letra)
        while 1:
            pos = so.recv(1024).decode()
            if pos == "end":
                break
            ahorcadol = list(ahorcado)
            ahorcadol[int(pos)] = letra
            
            ahorcado = "".join(ahorcadol)
    else:
        os.system("clear")
        
        print(ahorcado)
        print("\nVidas: 0")
        print("\nLetras usadas: "+str(letrasEscritas))
        print("Has perdido :(")
        
        break