# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:55:30 2022

@author: jose_santiago
"""
import random
import time
def dibujarTablero(tablero):
    #se dibuja el tablero
    print("***************")
    print('*    |   |    *')
    print('* ',tablero[7],'|',tablero[8],'|',tablero[9],' *')
    print('*    |   |    *')
    print('*  _________  *')
    print('*    |   |    *')
    print('* ',tablero[4],'|',tablero[5],'|',tablero[6],' *')
    print('*    |   |    *')
    print('*  _________  *')
    print('*    |   |    *')
    print('* ',tablero[1],'|',tablero[2],'|',tablero[3],' *')
    print('*    |   |    *')
    print("***************")
def ingresarLetraJugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        letra = input('¿Desea ser X o O?:').upper()
        #letra.upper() #upper convierte a mayusculas
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def quienComienza():
    if random.randint(0,1) == 0:
        return 'La computadora'
    else: 
        return 'El jugador'
def jugarDeNuevo():
    print('¿Desea volver a jugar? (si/no): ')
    return input().lower().startswith('s')
def hacerJugada(tablero,letra,jugada):
    tablero[jugada] = letra
def esGanador(ta,le): #ta es tablero y le es letra XD
    return ((ta[7]==le and ta[8]==le and ta[9]==le) or 
            (ta[4]==le and ta[5]==le and ta[6]==le) or 
            (ta[1]==le and ta[2]==le and ta[3]==le) or
            (ta[7]==le and ta[4]==le and ta[1]==le) or
            (ta[8]==le and ta[5]==le and ta[2]==le) or
            (ta[9]==le and ta[6]==le and ta[3]==le) or
            (ta[7]==le and ta[5]==le and ta[3]==le) or
            (ta[9]==le and ta[5]==le and ta[1]==le))
def obtenerDuplicadoTablero(tablero):
    dupTablero = []
    for i in tablero:
        dupTablero.append(i)
    return dupTablero
def hayEspacioLibre(tablero, jugada):
    return tablero[jugada] == ' ' 
def obtenerJugadaJugador(tablero):
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        jugada = int(input('¿Cual es tu proxima jugada? (1 - 9): '))
        return jugada
def elegirAzarDeLista(tablero, listaJugada):
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)
    if len(jugadasPosibles)!= 0:
        return random.choice(jugadasPosibles)
    else:
        return None
def obtenerJugadaComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'
    #Algoritmo de IA
    #verifica si podemos ganar en la proxima jugada
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i
    #verifica si el jugador podría ganar en su proxima jugada y lo bloquea
    for i in range(1,10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i
    #intenta ocupar unas de las esquinas libres
    jugada = elegirAzarDeLista(tablero, [1,3,7,9])
    if jugada != None:
        return jugada
    #De estar libre, intenta ocupar el centro
    if hayEspacioLibre(tablero, 5):
        return 5
    #time.sleep(1)
    #ocupa algunos de los lados
    return elegirAzarDeLista(tablero, [2,4,6,8])

def tableroCompleto(tablero):
    #regresa True si cada espacio del tablero fue ocupado
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True
# programa principal
print("*******Bienvenido al GATO ^.^*************")
while True:
    elTablero = [' ']*10 
    letraJugador, letraComputadora = ingresarLetraJugador()
    turno = quienComienza()
    print(turno, 'irá primero!')
    juegoEnCurso = True
    while juegoEnCurso:
        if turno == 'El jugador':
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades, has ganado! ...')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate! ...')
                    break
                else:
                    turno = 'La computadora'
        else:
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            time.sleep(1)#computadora pensando
            hacerJugada(elTablero, letraComputadora, jugada)
            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La computadora te ha vencido! has perdido ...')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print ('Es un empate! ...')
                    break
                else:
                    turno = 'El jugador'
    if not jugarDeNuevo():
        break