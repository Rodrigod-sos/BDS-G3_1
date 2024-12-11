#una a diferencia de un arreglo significa que es inmutable no podemos ni agregar 
#ni quitar valores pero sirve para aquellos valores que no cambian con el tiempo 

dias = ('lunes','martes','miercoles')
print(dias)

print('================================================')

print (type(dias))

#agregar valores a una tupla
dias=list(dias)  #cambiamos de tupla a lista 
print (type(dias))
dias[1]='jutiper'
dias.append('jueves')

dias=tuple(dias) #cambiamos de lista a tupla 

print(type(dias))
 
print('======================================')

#recorremos la tupla igual que la lista 
for dia in dias:
    print(dia)

print('============================================================')

#