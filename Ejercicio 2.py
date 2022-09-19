# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:34:26 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def esPrimo(numero):  # Funcion que determinará si el número entregado en el input es primo o no
    if numero <= 1:  # Si el número entregado es menor o igual que 1, no es primo
        return False

    # Comprobamos desde 2 a numero-1
    for i in range(2, numero):  # For loop que determinará si el número entregado es primo o no

        # Para determinar si el número es primo, el ciclo comprobará si el resto (%) de la división del número
        # entregado y el valor en la iteración es igual a 0, si igual a 0, no es primo, distinto de 0, es primo
        if numero % i == 0:
            # Como mencionado anteriormente, si el resto es 0, no es primo
            return False
    # Escapamos del ciclo y la función retorna True ya que se determinó que el numero si es primo
    return True


numero = int(input("Ingrese un número: "))
# Guardamos si el valor ingresado es primo o no en la variable 'resultado' con valor True o False
resultado = esPrimo(numero)

print(f"Los números primos menores que {numero} son: ")
for i in range(1, numero):  # Este ciclo irá revisando si los números entre 1 y n-1 son primos o no, en caso de serlo, lo omprime en pantalla
    if esPrimo(i):
        print(i)
