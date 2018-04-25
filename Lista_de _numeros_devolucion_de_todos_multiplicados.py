

lista_de_numeros = []
input_usuario = ""
total = 1

while len(lista_de_numeros) < 10:
    while not input_usuario.isdigit():
        input_usuario = input("Dime un número: ")
    lista_de_numeros.append(int(input_usuario))
    input_usuario = ""
    print("!Numero añadido¡")


for numero in lista_de_numeros:
    total = total * numero

print("El resultado  es {}".format(total))














