num1 = input("escribe el numero 1 : ")
num2 = input("escribe el numero 2 : ")

operacion = input ("escribe que operacion deseas ejecutar: Suma(s) o Resta(r)")

if (operacion == "s" ):
    suma = int(num1) + int(num2)
    print(f"La suma es: {suma} ")
elif (operacion == "r"):
    resta = int(num1) + int(num2)
    print(f"La suma es: {resta} ")
else:
    print("La operacion no existe ")

    exit()
    