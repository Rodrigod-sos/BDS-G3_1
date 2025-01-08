def suma(n1, n2): #es una funcion pero devuelve algo por ello el retun 
    resul =n1 + n2
    return resul

def suma_mensaje(n1,n2):
    resul = n1 + n2
    print(f'las suma de {n1} + {n2} es {resul}')

print("calculadora de suma")

n1=input("digite el priemro numero")
n2=input("digite el segundo numero")
suma1 = suma(int(n1),int(n2))
print(f'el resultado es {suma1}')

suma_mensaje(int(n1),int(n2))

