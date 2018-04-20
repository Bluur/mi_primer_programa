

mi_lista = []
input_usuario = ""
pregunta_usuario = ""
items_lista = 0

while input_usuario != "Fin":
    input_usuario = input("Dime una lista de palabras:  ").capitalize()
    if input_usuario != "Fin":
        mi_lista.append(input_usuario)


while pregunta_usuario != "No":
    pregunta_usuario = input("¿Quiéres saber cuanto mide tu lista?(Si/No): ").capitalize()
    if pregunta_usuario != "No":
        print("tu lista mide {}".format(len(mi_lista)))
    elif pregunta_usuario == "No":
        print("Hasta la próxima.")
    else:
        print("lo siento, te he pedido un si o un no")
    break
while pregunta_usuario != "No":
    pregunta_usuario = input("¿Quiéres saber cuanto mide cada objeto de la lista?(Si/No): ").capitalize()
    if pregunta_usuario != "No":
        for item in mi_lista:
            len(mi_lista[items_lista])
            print("El objeto {} mide {}".format(item, len(mi_lista[items_lista])))
            items_lista += 1
    elif pregunta_usuario == "No":
        print("Hasta la proxima")
    else:
        print("lo siento, te he pedido un si o un no")
    break
print("¡Hasta la vista!")



















