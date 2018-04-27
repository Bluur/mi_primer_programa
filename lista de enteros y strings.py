
lista_mixta = []
lista_enteros = []
lista_strings = []
input_usuario = ""

while input_usuario != "Fin":
    input_usuario = input("Dime una secuencia de numeros y strings: ")

    if input_usuario > 0:
        for numero in input_usuario:
            if numero in input_usuario:
                numero = int()
                lista_enteros.append(numero)
                print("Esta es la lista de numeros enteros que habia en tu secuencia{} ".format(lista_enteros))

    elif input_usuario == type(str):
        for string in input_usuario:
            if string in input_usuario:
                string = ""
                lista_strings.append(string)
                print("Esta es la lista de Strings que había en tu secuencia{} ".format(lista_strings))

    else:
        print("No me vale, dame un numero o una string")
