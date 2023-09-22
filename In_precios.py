#!/usr/bin/env python3
from colorama import init, Fore, Style, Back
init()
from time import sleep
import os

global lista
lista = list()

def compras():
    os.system("clear")
    i = 0
    total = 0
    cant = int(input("\n\ncantidad de productos a ingresar?? : "))
    while i < cant:
        i += 1
        precio = int(input(f"\n\nProducto: {i} Ingrese precio: "))
        print("ingrese solo valores enteros (sin puntos)")
        total += precio
        lista.append(precio)
    print(f"\nEl total es: {total} y los productos son {i}")
    input("para volver al menu press (enter): ")


def verProductos():
    os.system("clear")
    print("\t\t\t\t\n\n*** Los precios ingresados son ***")
    print("\nLos precio de los articulos comprados son:")
    for i in lista:
        print(i)
    input("para volver al menu press (enter): ")
    


if __name__ == '__main__':
    while True:
        os.system("clear")
        print(Fore.WHITE+Style.BRIGHT+"          ?       __MENU__        ?     ")
        menu = """
        ==============================
        [[ Created by: Hans Saldias ]]
        [[                          ]]
        [[ by: 1LugarParaProgramar  ]]
        ==============================

        [1] ingreso de productos
              
        [2] ver productos ingresados      
              
        [00] salir ...
        """
        for i in menu:
            print(i, end="", flush=True)
            sleep(0.1)
        op = int(input("Ingrese opcion: "))
        if op == 1:
            compras()
        elif op == 2:
            verProductos()
        elif op == 00:
            print("gracias por usar mi script")
            break
        else:
            print("opcion ingresada no svalida")



