
mi_lista = []
input_usuario = ''

while input_usuario != 'FIN':
    input_usuario = input('¿Que necesitas comprar?(Escribe FIN para salir): ').upper()
    if input_usuario != 'FIN':
        mi_lista.append(input_usuario)


numero_de_objetos = len(mi_lista)
indice_actual = 0

#Esta funcion de aqui abajo la he sacado yo antes de ver el tutorial, en le cual nate explica a hacerlo con while

print('Hay {} cosas en tu lista de la compra'.format(numero_de_objetos))
#Esta es la primera opcion para que cuente lo que hay dentro de la lista, es mas larga y dificil pero saca del apuro.+

#while indice_actual < numero_de_objetos:
    #print(' tengo que comprar {}'.format(mi_lista[indice_actual]))
    #indice_actual += 1

#Esta es la segunda funcion para que cuente lo que hay dentro de la lista (es mas limpia y queda mas 'profesional')

for item in mi_lista:
    print('Tengo que comprar {} '.format(item))

print('Esta es la lista de la compra')
