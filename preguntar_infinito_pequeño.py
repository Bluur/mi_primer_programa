"""
Pregunta a el usuario una serie de 10 numeros, determina cual es el más pequeño de los 10
"""

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("!Numero añadido¡")

numero_pequeño = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeño:
        numero_pequeño = numero

print("El numero más pequeño es {}".format(numero_pequeño))