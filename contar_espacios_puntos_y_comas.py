
frase_del_usuario = input("Introduce una frase: ")

punto = ["."]
coma = [","]
espacio = [" "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for letra in frase_del_usuario:
    if letra in punto:
        n_puntos += 1
    elif letra in coma:
        n_comas += 1
    elif letra in espacio:
        n_espacios += 1

print("Hay {} puntos, {} comas y {} espacios".format(n_puntos, n_comas, n_espacios))

