import os
from time import sleep

"""
CRUD para gestión de empresas
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

dic_empresas = {
    '12345678901': {
        'razon_social': 'Empresa XYZ',
        'direccion': 'Av. Principal 123'
    }
}

ANCHO = 50
opcion = 0

while opcion != 5:
    os.system("clear")
    print("=" * ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("=" * ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    try:
        opcion = int(input("INGRESE OPCIÓN: "))
    except ValueError:
        print("Ingrese un número válido.")
        sleep(1)
        continue

    os.system("clear")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("RUC: ")
        if len(ruc) != 11 or not ruc.isdigit():
            print("El RUC debe tener 11 dígitos.")
            sleep(1)
            continue
        if ruc in dic_empresas:
            print("Esta empresa ya está registrada.")
            sleep(1)
            continue
        razon_social = input("Razón Social: ")
        direccion = input("Dirección: ")
        dic_empresas[ruc] = {
            'razon_social': razon_social,
            'direccion': direccion
        }
        print("Empresa registrada con éxito!")
        sleep(1)

    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        if not dic_empresas:
            print("No hay empresas registradas.")
        else:
            for ruc, datos in dic_empresas.items():
                print(f"RUC: {ruc}")
                print(f"Razón Social: {datos['razon_social']}")
                print(f"Dirección: {datos['direccion']}")
                print("*" * ANCHO)
        input("Presione ENTER para continuar...")

    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa a actualizar: {dic_empresas[ruc]['razon_social']}")
            nueva_razon_social = input("Nueva Razón Social: ") or dic_empresas[ruc]['razon_social']
            nueva_direccion = input("Nueva Dirección: ") or dic_empresas[ruc]['direccion']
            dic_empresas[ruc] = {
                'razon_social': nueva_razon_social,
                'direccion': nueva_direccion
            }
            print("Empresa actualizada con éxito!")
        else:
            print("Empresa no encontrada.")
        sleep(1)

    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada con éxito!")
        else:
            print("Empresa no encontrada.")
        sleep(1)

    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("=" * ANCHO)
        print("Saliendo del sistema...")
    else:
        print("=" * ANCHO)
        print(" " * 10 + "OPCIÓN INVÁLIDA!!!")
        print("=" * ANCHO)
        sleep(1)
