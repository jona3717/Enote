#!/usr/bin/python

#Este módulo contiene las funciones que realiza Enote

import os, time


def crear():
    #Crea una nota y le asigna el nombre indicado por el usuario

    print('Ingresa el contenido de la nota y pulsa enter al terminar.')
    print('----------------------------------------------------------')
    print('')
    nueva_nota = input(str())
    a = open('/opt/Enote/notas/nota.txt', 'w')
    a.write(nueva_nota)
    a.close()
    print('')
    print('############################')
    print('Inserta el nombre de la nota')
    print('')
    nombre_nota = input(str())
    os.rename('/opt/Enote/notas/nota.txt', '/opt/Enote/notas/{}.txt'.format(nombre_nota))


def eliminar():
    #Elimina la nota especificada por el usuario

    print('Ingresa el nombre de la nota que quieres eliminar')
    print('Para volver ingresa [q]')
    print('=================================================')
    print('')
    lista = os.listdir('/opt/Enote/notas')
    print('')
    i=0
    for i in lista:
        print('- '+i)
    print('')
    nota_eliminar = input(str(''))
    if nota_eliminar != 'q':
        if not os.path.isfile('/opt/Enote/notas/'+nota_eliminar+'.txt'):
            print('')
            print('########################################')
            print('La nota que intentas eliminar no existe.')
            time.sleep(2)
            os.system('clear')
            eliminar()
        else:
            os.remove('/opt/Enote/notas/'+nota_eliminar+'.txt')
            print('')
            print('##########################')
            print('La nota ha sido eliminada.')
            time.sleep(1.5)
            pass
    else:
        pass
        

def lista_notas():
    #Muestra las notas existentes.

    lista = os.listdir('/opt/Enote/notas')
    print('Para volver pulsa enter')
    print('-----------------------')
    print('')
    i=0
    for i in lista:
        print('- '+i)
    #print(lista)
    print('')
    input(str())


def modificar():
    #Modifica notas existentes.

    print('* Indica el nombre de la nota que quieres ver o modificar.')
    print('----------------------------------------------------------')
    print('')
    lista = os.listdir('/opt/Enote/notas')
    print('')
    i=0
    for i in lista:
        print('- '+i)
    print('')
    print('#######################')
    print('* Para volver pulsa [q]')
    print('')
    nota = input(str())
    local = '/opt/Enote/notas/'
    nota_mod = local+nota+'.txt'
    if os.path.isfile(nota_mod):
        if not os.path.isfile(local + nota + '.txt'):
            os.system('clear')
            print('#######################################')
            print('La nota especificada no existe.')
            print('')
            time.sleep(1.7)
            modificar()
        else:
            os.system('clear')
            print('##########################################')
            print('* Para ver la nota sin modificarla pulsa [1]')
            print('* Para modificar la nota pulsa [2]')
            print('* Para volver pulsa [q]')
            print('')
            opcion = input(str())
            if opcion == '1':
                os.system('clear')
                loc_nota = local+nota+'.txt'
                abre_nota = open(loc_nota, 'r')
                leer_nota = abre_nota.read()
                print('#########################################')
                print('')
                print(leer_nota)
                print('')
                print('#########################################')
                print('')
                abre_nota.close()
                input(str('Pulsa enter para volver.'))
                os.system('clear')
                modificar()
            elif opcion == '2':
                os.system('clear')
                os.system('micro ' + nota_mod)
                modificar()
            elif opcion == 'q':
                os.system('clear')
                modificar()
            else:
                os.system('clear')
                print('')
                print('#################################')
                print('El valor ingresdado no es válido.')
                print('')
                time.sleep(1.7)
                modificar()
                os.system('micro'+nota)
    elif nota == 'q':
        pass
    else:
        print('')
        print('########################################')
        print('La nota que intentas modificar no existe.')
        time.sleep(2)
        modificar()


def menu():
    #Un menú de opciones que se muestra al iniciar Enote
    
    opciones = {1:'Nueva Nota',
                2:'Eliminar Nota',
                3:'Lista de Notas',
                4:'Ver y Modificar Notas',
                'q':'Salir de Enote'}
    print('1.'+opciones[1])
    print('2.'+opciones[2])
    print('3.'+opciones[3])
    print('4.'+opciones[4])
    print('q.'+opciones['q'])
        