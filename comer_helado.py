
apetece_helado_input = input('¿Te apetece un helado? (si/no): ').upper()
tiene_dinero_input = input('¿Tienes dinero para un helado? (si/no): ').upper()
esta_el_heladero_input = input('¿Esta el señor de los helados? (Si/no): ').upper()
esta_tu_tia_input = input('¿Estas con tu tia? (si/no): ').upper()

apetece_helado = apetece_helado_input == 'SI'
tiene_dinero = tiene_dinero_input == 'SI'
esta_tu_tia = esta_tu_tia_input == 'SI'
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_heladero = esta_el_heladero_input == 'SI'

if apetece_helado and puede_permitirselo and esta_el_heladero:
    print('Pues comete un helado')
else:
    print('Pues nada')