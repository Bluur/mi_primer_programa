
mi_lista = ['lechuga', 'tomate', 'helado', 'pan', 'pasta', 'olivas', 'atun', 'fanta']

numero_de_objetos = len(mi_lista)
indice_actual = 0

#Esta funcion de aqui abajo la he sacado yo antes de ver el tutorial, en le cual nate explica a hacerlo con while

print('El numero de cosas que hay en tu lista es de {}'.format(numero_de_objetos))

while indice_actual < numero_de_objetos:
    print(' tengo que comprar {}'.format(mi_lista[indice_actual]))
    indice_actual += 1
print('esta es la lista de la comprar ')
#minuto del video 14:01