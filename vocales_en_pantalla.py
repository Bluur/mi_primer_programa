
texto_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]
vocales_texto = []
n_vocales = 0

for letra in texto_usuario:
    if letra in vocales:
        vocales_texto.append(letra)
print("vocales = {}".format(vocales_texto))
