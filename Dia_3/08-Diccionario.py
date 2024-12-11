capitales = {
 'peru' : 'lima',
 'colombia': 'bogota',
 'chile':'santiago'

}

print(capitales['chile'])
print('================================================')
#pais=input('digite su pais : ')
#capitales = pais.get(pais)
#print(f'La capital de {pais} es {capitales} ')

#aplicacion

pais =input('digite un pais')
if pais in capitales:
    capital=capitales.get(pais)
    print(capital)

    eliminar_capital=('desea eliminar la capital?: si(s) ')
    if eliminar_capital == "s":
        capitales.pop(pais,'no existe')
        print(capitales)
else:
    print('capital no encontrada :,V ')
    agregar_capital =input('desea agregar su capital')
    if agregar_capital == 's':
        nueva_capital=input('ingrese capital:')

        capitales.update({pais:nueva_capital})
        print(capitales)

