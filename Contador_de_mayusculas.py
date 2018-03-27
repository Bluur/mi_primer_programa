
texto_usuario = input("Introduce una frase: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R","S","T","U"
              "V", "W","X","Y", "Z"]

n_mayusculas = 0

for letra in texto_usuario:
    if letra in mayusculas:
        n_mayusculas += 1

print("Hay {} mayúsculas".format(n_mayusculas))

