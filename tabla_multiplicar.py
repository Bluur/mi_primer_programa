#Más tarde, viendo la web de python para hace la tabla inversa me di cuenta de que haciendo {for multiplo in range(1,11,2)}hace los multiplos de 2 sin necesidad de insertar mas numero o mas codigo :S
"""
Obtener la tabla de multiplicar de un numero especificado por el usuario
"""

numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))
#este ejercicio esta echo para que solo muestre multiplos de 2 en la tabla del 3, borra la lista y variable de aqui abajo
#y en el format de abajo de eltodo cambia a multiplo * numero_tabla.
multiplos_de_2 = [6,12,18,24,30]
multiplos_de_3 = 0
for multiplo in range(1,11):
    multiplos_de_3 = numero_tabla * multiplo
    if multiplos_de_3 in multiplos_de_2:
        print("{} x {} = {}".format(multiplo, numero_tabla, multiplos_de_3))








