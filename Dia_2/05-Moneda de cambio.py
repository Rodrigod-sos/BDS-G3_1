
print("Conversión de monedas")
print("------------------------------")
print("1. De soles a dólares")
print("2. De dólares a soles")
print("                                  ")
    
opcion = input("Selecciona una opción (1 o 2): ")

if opcion == "1":
        soles = float(input("Ingresa la cantidad en soles: "))
        dolares = soles / 3.71
        print(f"{soles} soles equivalen a {dolares} dólares.")
elif opcion == "2":
        dolares = float(input("Ingresa la cantidad en dólares: "))
        soles = dolares * 3.71
        print(f"{dolares} dólares equivalen a {soles} soles.")

else:
     print("Opción inválida. Por favor, selecciona 1 o 2.")
