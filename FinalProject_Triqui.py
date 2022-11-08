#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:19:28 2022

@author: lmordoneze
"""

"""Para este proyecto, deberás programar el juego TA-TE-TI. Cuando el programa
comienza a correr, en la pantalla aparece el tablero de TA-TE-TI (de 3x3) y un
input que permite al usuario elegir el símbolo “X” o el símbolo “O”. Las “X”
empiezan. El usuario debe elegir la posición del tablero (esta posición debe
ser correcta y no debe estar ocupada) donde poner el símbolo en el tablero y el
sistema valida si el juego termina con un ganador o en empate. Si no hay ganador
o la partida no terminó todavía en empate, el juego continúa preguntando al otro
usuario que seleccione la posición del tablero dónde quiere poner su símbolo y
así siguiendo hasta que la partida termine con un ganador o en empate.

Notas:
Representar el tablero como una matriz de 3x3.
El juego termina en empate cuando el tablero está completo y no hay ganadores.
Ejemplo de dibujo de tablero vacío:

|_|_|_|
|_|_|_|
|_|_|_|

Ejemplo de dibujo en pantalla tablero completo: 

|X|X|O|
|O|O|X|
|X|X|O|"""

from time import sleep
from os import system

matriz = [["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]]

matriz_guia = [["0.0","0.1","0.2"],
          ["1.0","1.1","1.2"],
          ["2.0","2.1","2.2"]]

def limpiar_matriz():
    for fil in range(3):
        for col in range(3):
            matriz[fil][col] = "-"
    
def mostrar_tablero():
	print("Tablero de Juego                 Tablero Guia")
	print("\n{", matriz[0][0], "}", "{", matriz[0][1], "}", "{", matriz[0][2], "}", "         ", "{", matriz_guia[0][0], "}", "{", matriz_guia[0][1], "}", "{", matriz_guia[0][2], "}")
	print("{", matriz[1][0], "}", "{", matriz[1][1], "}", "{", matriz[1][2], "}", "         ", "{", matriz_guia[1][0], "}", "{", matriz_guia[1][1], "}", "{", matriz_guia[1][2], "}")
	print("{", matriz[2][0], "}", "{", matriz[2][1], "}", "{", matriz[2][2], "}", "         ", "{", matriz_guia[2][0], "}", "{", matriz_guia[2][1], "}", "{", matriz_guia[2][2], "}")
	
def leer_numero():   
    controlador = 0
    while controlador == 0:
        x = input("Ingrese número: ")
        try:
            int(x)
            if int(x) < 0 or int(x) > 2:
                print("Vuelve a intentarlo")
            else:
                controlador = 1
        except ValueError:
            print("Vuelve a intentarlo")
    return int(x)
    
def instrucciones():
    print("""Sean bienvenidos a jugar triki. Las instrucciones son muy simples:
        Gana el que alinee 3 de sus simbolos.
        Usted no ingresara el simbolo, sino que, ingresara la posicion de la casilla. 
        Primero se ingresa la fila que son las lineas horizontales (van de 0 a 2), luego la
        columna que son las lineas verticales (van de 0 a 2). Ejemplo: Si yo quiero poner en
        la casilla de la esquina superior derecha. Debo ingresar la fila 0 y la columna 2.
        Puede ver el tablero guia con las coordenadas de las posiciones para mayor facilidad. 
        Siempre inicia la x. Asi que... A jugar\n\n""")
        
def seguir_jugando():
    x = int(input("¿Desea seguir jugando?\n\nSi: 1\nNo: 2\n\nIngrese número: "))
    return x 

def validar_casilla_ocupada(fil, col):
    if matriz[fil][col] != '-':
        print("Casilla ocupada.")
        return True
    else:
        return False

def ganador():
    	if matriz[0][0] == 'x' or matriz[0][0] == 'o':
            if matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2]: # primera fila
                if matriz[0][0] =='x':
                    return 0 # gano jugador que tiene el simbolo x
                if matriz[0][0]=='o':
                    return 1 # gano jugador que tiene el simbolo o
            if matriz[0][0]==matriz[1][0] and matriz[0][0]==matriz[2][0]: # primera columna
                if matriz[0][0]=='x':
                    return 0
                if matriz[0][0]=='o':
                    return 1
            if matriz[1][1]==matriz[0][0] and matriz[1][1]==matriz[2][2]: #primera diagonal
                if matriz[1][1]=='x':
                    return 0
                if matriz[1][1]=='o':
                    return 1
            if matriz[1][1]==matriz[0][1] and matriz[1][1]==matriz[2][1]: #segunda columna
                if matriz[1][1]=='x':
                    return 0
                if matriz[1][1]=='o':
                    return 1
            if matriz[1][1]==matriz[2][0] and matriz[1][1]==matriz[0][2]: #segunda diagonal
                if matriz[1][1]=='x':
                    return 0
                if matriz[1][1]=='o':
                    return 1
            if matriz[1][1]==matriz[1][0] and matriz[1][1]==matriz[1][2]: # segunda fila
                if matriz[1][1]=='x':
                    return 0
                if matriz[1][1]=='o':
                    return 1
            if matriz[2][2]==matriz[0][2] and matriz[2][2]==matriz[1][2]: # tercera columna
                if matriz[2][2]=='x':
                    return 0
                if matriz[2][2]=='o':
                    return 1
            if matriz[2][2]==matriz[2][0] and matriz[2][2]==matriz[2][1]: # tercera fila
                if matriz[2][2]=='x':
                    return 0
                if matriz[2][2]=='o':
                    return 1

def modificar_matriz(fil, col, simbolo):
    matriz[fil][col] = simbolo

# Desde aquí empieza el código
instrucciones()
mostrar_tablero()

sw = 0
while sw == 0:
    print("\n\nEl que primero selecciona es el jugador #1. Jugador, selecciona tu símbolo.\n1: X\n2: O")
    jugador1 = leer_numero()
    print("\nJugador #2, Selecciona tu simbolo.")
    jugador2 = leer_numero()
    if jugador1 == 0 or jugador2 == 0:
        print("\nAmbos, o alguno, escogió el cero. Vuelvan a intentarlo.")
    else:
        sw = 1
        
if jugador1 == 1:
    print("\nJugador 1: x\nJugador 2: o\n\nInicia el jugador 1\n")
else:
    print("\nJugador 1: o\nJugador 2: x\n\nInicia le jugador 2\n")

if jugador1 == 1: # El jugador 1 tiene la x
    jugador = 1
else:
    jugador = 2 # El jugador 2 tiene la x

simbolo = "x"
cont = 0
n = 0
empate = 0 # Inicia en empate
while n < 9:
    print("Turno del jugador", jugador, "\n")
    mostrar_tablero()
    print("\nSelecciona la fila")
    fila = leer_numero()
    print("\nSelecciona la columna")
    columna = leer_numero()
    while validar_casilla_ocupada(fila, columna) == True:
        sleep(2)
        system('clear')
        mostrar_tablero()
        print("\nSelecciona la fila")
        fila = leer_numero()
        print("\nSelecciona la columna")
        columna = leer_numero()
    modificar_matriz(fila, columna, simbolo)
    n += 1
    cont += 1
    if cont > 4:
        if ganador() == 0 and jugador2 == 1:
            print("Ganó el jugador 2") # gano jugador que tiene el simbolo x
            mostrar_tablero()
            empate = 1 #No hay empate
            if seguir_jugando() == 1: #Seguiran jugando
                n = 0 # De esta forma el ciclo while inicia desde 0
                cont = 0 # y se reinicia todo
                empate = 0
                limpiar_matriz()
            else:
                break
        if ganador() == 1 and jugador2 == 2:
            print("Ganó el jugador 2") # gano jugador que tiene el simbolo o
            mostrar_tablero()
            empate = 1
            if seguir_jugando() == 1:
                n = 0
                cont = 0
                empate = 0
                limpiar_matriz()
            else:
                break
        if ganador() == 0 and jugador1 == 1:
            print("Ganó el jugador 1") # gano jugador que tiene el simbolo x
            mostrar_tablero()
            empate = 1
            if seguir_jugando() == 1:
                n = 0
                cont = 0
                empate = 0
                limpiar_matriz()
            else:
                break
        if ganador() == 1 and jugador1 == 2:
            print("Ganó el jugador 1") # gano jugador que tiene el simbolo o
            mostrar_tablero()
            empate = 1
            if seguir_jugando() == 1:
                n = 0
                cont = 0
                empate = 0
                limpiar_matriz()
            else:
                break
    sleep(1)
    system('clear')
    if jugador == 1:
        jugador = 2
    elif jugador == 2:
        jugador = 1
    if simbolo == "x":
        simbolo = "o"
    elif simbolo == "o":
        simbolo = "x"
if empate == 0 and n == 9:
    mostrar_tablero()
    print("\nEmpate")
if empate == 1:
    print("Juego terminado")