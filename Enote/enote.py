#!/usr/bin/python

"""Enote es una aplicación de consola para crear notas, estas son almacenadas en
formato .txt de manera local. Por el momento Enote solo trabaja en CLI, esperao añadir
nuevas características más adelante."""

import funciones,os,time,os.path,sys


def ini_enote():
    os.system('clear')
    print('Enote')
    print('=====')
    print('')
    funciones.menu()
    print('')
    opcion = input(str())
    if opcion == '1':
        os.system('clear')
        funciones.crear()
    elif opcion == '2':
        os.system('clear')
        funciones.eliminar()
    elif opcion == '3':
        os.system('clear')
        funciones.lista_notas()
    elif opcion == '4':
        os.system('clear')
        funciones.modificar()
    elif opcion == 'q':
        os.system('clear')
        sys.exit()
    else:
        print('')
        print('###################')
        print('Ingreso incorrecto.')
        time.sleep(1)
        return ini_enote()

def inicio():
    if not os.path.exists('/opt/Enote/notas/'):
        os.system('mkdir -p /opt/Enote/notas/')
    else:
        pass

while True:
    inicio()
    ini_enote()
    