
lista_mixta = []
lista_enteros = []
lista_strings = []
input_usuario = ""

while input_usuario != "Fin":
    input_usuario = input("Dime una secuencia de numeros y strings: ")

    if input_usuario > 0:
        for item in input_usuario:

                if type(item) == str:

                    lista_strings.append(item)

                elif type(item) == int:

                    lista_enteros.append(item)

    else:
        print("No me vale, dame un numero o una string")
