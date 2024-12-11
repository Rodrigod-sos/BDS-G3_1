capitales = {
 'peru' : 'lima',
 'colombia': 'bogota',
 'chile':'santiago'

}

print('='*50)
#recorrido por claves 
for clave in capitales.keys():
    print(clave)

print('='*50)

#reccorido por valores 
for valores in capitales.values():
    print(valores)

print('='*50)

#recorrido por claves,valor 
for clave,valores in capitales.items():
    print(f'la capital de {clave} es {valores} ')

