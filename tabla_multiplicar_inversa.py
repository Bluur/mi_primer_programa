
tabla_elegida = int(input("Introduce la tabla de multiplicar que desees saber inversamente: "))

for multiplo in range(10, 0, -1):
    print("{} x {} = {}".format(tabla_elegida, multiplo, multiplo * tabla_elegida))