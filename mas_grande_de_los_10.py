"""
Pregunta al usuario una serie de 10 numeros, determina cual es el mas grande de los 10
"""

numeros_usuario = []
input_usuario = ""

while input_usuario != "Fin":
    input_usuario = input("Dime los numeros que deseas comparar: ").capitalize()
    if input_usuario != "Fin":
        numeros_usuario.append(input_usuario)
    elif input_usuario == "Fin":
        print(max(numeros_usuario))









