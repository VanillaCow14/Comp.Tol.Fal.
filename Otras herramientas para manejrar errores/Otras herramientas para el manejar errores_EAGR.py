#Como manejar la division entre 0 con if

def division(a, b):
    if b != 0:
        res = a / b
        return res
    else:
        print("Error: No se puede dividir entre 0.")
        return None

num = float(input("Ingrese el numero: "))
div = float(input("Ingrese el divisor: "))

res = division(num, div)

if res is not None:
    print("El resultado de la división es:", res)

#Como manejar la division entre 0 con try except

def dividir(num,div):
  return num/div
try:
    res = dividir(19, 0)
    print(res)
except ZeroDivisionError:
    print("Error dividir entre 0 no es posible… ")