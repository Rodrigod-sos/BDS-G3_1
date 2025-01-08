condicion = "si"
while (condicion == "si") :

    num_1=input("Digite el numero 1: ")
    num_2=input("Digite el numero 2: ")
    print("===========CALCULADORA==============")

    print(""" Selecciona una opcion:
        [1]--SUMA 
        [2]--RESTA
        [3]--MULTIPLICACION 
        [4]--DIVISION 
        """)

    opcion=input("")

    if (opcion == "1"):
        print(f'La suma de {num_1} + {num_2} = {int(num_1) + int(num_2)}')
    elif (opcion == "2"):
        print(f'La resta de {num_1} - {num_2} = {int(num_1) - int(num_2)}')
    elif (opcion == "3"):
        print(f'La multiplicacion de {num_1} * {num_2} = {int(num_1) * int(num_2)}')
    elif (opcion == "4"):
        print(f'La division de {num_1} / {num_2} = {int(num_1) / int(num_2)}')
    else:
        print("operacion no encontrada")
    condicion=input("desea continuar (si/no)")