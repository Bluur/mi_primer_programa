

mi_lista = []
lista_de_largos = []
input_usuario = ""
pregunta_usuario = ""
items_lista = 0

while input_usuario != "Fin":
    input_usuario = input("Dime una lista de palabras(Escribe Fin para acabar):  ").capitalize()
    if input_usuario != "Fin":
        mi_lista.append(input_usuario)


while pregunta_usuario != "No":
    pregunta_usuario = input("¿Quiéres saber cuanto mide tu lista?(Si/No): ").capitalize()
    if pregunta_usuario != "No":
        print("tu lista mide {} palabra/s de largo".format(len(mi_lista)))
    elif pregunta_usuario == "No":
        print("Hasta la próxima.")
    else:
        print("lo siento, te he pedido un si o un no")
    break
while pregunta_usuario != "No":
    pregunta_usuario = input("¿Quiéres saber cuanto mide cada palabra de la lista?(Si/No): ").capitalize()
    if pregunta_usuario != "No":

        for item in mi_lista:
            len(mi_lista[items_lista])
            print("La palabra {} mide {} caracteres".format(item, len(mi_lista[items_lista])))
            lista_de_largos.append(len(mi_lista[items_lista]))
            items_lista += 1
        print("Tu lista de largos es {}".format(lista_de_largos))

    elif pregunta_usuario == "No":
        print("Hasta la proxima")
    else:
        print("lo siento, te he pedido un si o un no")
    break
print("¡Hasta la vista!")



















