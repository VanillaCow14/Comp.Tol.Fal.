import threading

#suma
def suma(a, b):
    result = a + b
    print(f"Suma: {a} + {b} = {result}")

#resta
def resta(a, b):
    result = a - b
    print(f"Resta: {a} - {b} = {result}")

#multiplicación
def multiplicacion(a, b):
    result = a * b
    print(f"Multiplicación: {a} * {b} = {result}")

#división
def division(a, b):
    if b != 0:
        result = a / b
        print(f"División: {a} / {b} = {result}")
    else:
        print("No se puede dividir por cero.")
        b = int(input("Ingresa de nuevo el numero:"))
        result = a / b
        print(f"{result}")

#Ingreso de datos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Crear hilos para realizar operaciones
suma_thread = threading.Thread(target=suma, args=(num1, num2))
resta_thread = threading.Thread(target=resta, args=(num1, num2))
multiplicacion_thread = threading.Thread(target=multiplicacion, args=(num1, num2))
division_thread = threading.Thread(target=division, args=(num1, num2))

# Iniciar los hilos
suma_thread.start()
resta_thread.start()
multiplicacion_thread.start()
division_thread.start()

# Ejecutar hilos
suma_thread.join()
resta_thread.join()
multiplicacion_thread.join()
division_thread.join()

print("Todas las operaciones han sido ejecutadas.")
