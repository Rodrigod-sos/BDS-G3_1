#parametros arg y kwargs

def sumar_infinitos(*args):
    resultado = 0 
    for numero in args:
        resultado=resultado + numero
    return resultado

suma1 = sumar_infinitos(1,2,3,4,5)
print(f'la suma de suma 1 es {suma1}')


def calculadora(**kwargs):
    ope=kwargs.get('ope')
    n1=kwargs.get('n1')
    n2=kwargs.get('n2')

    if ope== 'suma':
        resul=n1+n2
        return resul
    elif ope== 'resta':
        resul=n1-n2
        return resul
    else:
        print("no hay oprador")
        resul='error'
        return resul


suma2=calculadora(n1=2,n2=1,ope='rtgn')
print(f'el resultado es {suma2}')

