
apetece_helado_input = input('¿Te apetece un helado? (si/no): ').upper()

if apetece_helado_input == 'SI':
    apetece_helado = True
elif apetece_helado_input == 'NO':
    apetece_helado = False
else:
    print('Te he dicho que me digas si o no, no se que has dicho pero cuento como que no')
    apetece_helado = False

tiene_dinero_input = input('¿Tienes dinero para un helado? (si/no): ').upper()
esta_el_heladero_input = input('¿Esta el señor de los helados? (Si/no): ').upper()
esta_tu_tia_input = input('¿Estas con tu tia? (si/no): ').upper()

tiene_dinero = tiene_dinero_input == 'SI'
esta_tu_tia = esta_tu_tia_input == 'SI'
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_heladero = esta_el_heladero_input == 'SI'

if apetece_helado and puede_permitirselo and esta_el_heladero:
    print('Pues comete un helado')
else:
    print('Pues nada')