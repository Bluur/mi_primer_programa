

mi_lista = []
input_usuario = ""
pregunta_usuario = ""

while input_usuario != "Fin":
    input_usuario = input("Dime una lista de palabras:  ").capitalize()
    if input_usuario != "Fin":
        mi_lista.append(input_usuario)

print("Tu lista mide {}".format(len(mi_lista)))


while pregunta_usuario != "No":
    pregunta_usuario = input("¿Quiéres saber cuanto mide cada palabra?(Si/No): ").capitalize()
    if pregunta_usuario  != "No":
        print(len)
    elif pregunta_usuario == "No":
        print("Hasta la proxima")
    else:
        print("lo siento, te he pedido un si o un no")


















