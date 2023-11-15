#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
from enum import Enum

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

class Opcion(Enum):
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3

#a function that return a aleatory number between 1 and 3
def num_aleatory():
    return random.randint(1,3)

salir = True
victorias = 0
rondas = 0

while(salir == True):

    print('Selection una opcion:\n'
          + '1 --> Piedra \n'
          + '2 --> Papel \n'
          + '3 --> Tijera ')

    try:
        request = int(input("Ingrese un numero entre 1 y 3: "))

        if(request < 1 or request > 4):
            print("\n -----------Por favor ingrese un numero valido-----------\n")
            continue

        #if the user select a number between 1 and 3
        if(request > 0 and request < 4):
            print("\nSu seleccion es: " + Opcion(request).name )

            #get the aleatory number
            aleatory = num_aleatory()

            print("La seleccion del computador es: " + Opcion(aleatory).name + "\n")

            #if the user and the computer select the same option
            if(request == aleatory):
                print("Empate\n")
            else:
                #if the user select rock
                if(request == 1):
                    if(aleatory == 2):
                        print("Perdiste\n")
                    else:
                        print("Ganaste\n")
                        victorias += 1
                #if the user select paper
                elif(request == 2):
                    if(aleatory == 1):
                        print("Ganaste\n")
                        victorias += 1
                    else:
                        print("Perdiste\n")
                #if the user select scissors
                elif(request == 3):
                    if(aleatory == 1):
                        print("Perdiste\n")
                    else:
                        print("Ganaste\n")
                        victorias += 1 
    except ValueError:
        print("\n -----------Por favor ingrese un numero valido-----------\n")
        continue

    print("Desea continuar jugando?")
    print("1 --> Si ")
    print("2 --> No \n")

    if(int(input()) == 2):
        salir = False

    rondas += 1

print("\nPuntuacion: " + str(victorias) + " | rondas: " + str(rondas))