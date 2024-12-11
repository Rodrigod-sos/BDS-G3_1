dias=['lunes','martes','miercoles','jueves','viernes','sabado']
print(dias[1])
print(dias[-1])  #los arreglos pueden ser negativos por que estan en forma circular de modo que el -1 es el ultimo valor del arrglo 
print(dias[1:3]) #esto imprime los arreglos pero en un rango 

print('============================================================================')

#agregar valores a un arreglo 
dias.append('domingo')
print(dias)
print('============================================================================')

#eliminar valores 
dias.pop(6)
print(dias)
del dias[0:2]  #eliminas pero en un rango 

print('============================================================================')

#actualizar un valor 
dias[4] ='saturno'
print(dias) 

print('============================================================================')

#recorrer un arreglo 
for contador in range(len(dias)):  #len(dias) me muestra la longitud de nuestro arreglo dias 
    print(contador)

print('============================================================================')

    #forma sencilla que recorre una variable dia en dias 
for dia in dias: 
    print(dia)


