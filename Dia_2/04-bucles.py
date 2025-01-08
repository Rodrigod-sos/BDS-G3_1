#bucle for
tabla=input("tabla de multiplicar: ")
print("====================================")
for contador in range(1,15,1):
    print(f'{tabla} x {contador} = {int(tabla) * contador}')
