

lista_de_numeros = []
input_usuario = ""

while len(lista_de_numeros) < 10:
    while not input_usuario.isdigit():
        input_usuario = input("Dime un número: ")
    lista_de_numeros.append(int(input_usuario))
    input_usuario = ""
    print("!Numero añadido¡")


for numero in input_usuario:
    if numero > 0:
        lista_de_numeros.append(numero)











