import os
print ("Este programa simula un login que al cerrar terminal para no perder datos guarda estos datos en un archivo")

def guardar_login(usuario, contrasena):
    with open("login.txt", "w") as archivo:
        archivo.write(f"Nombre de usuario: {usuario}\n")
        archivo.write(f"Contraseña: {contrasena}\n")

def cargar_login():
    try:
        with open("login.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= 2:
                usuario = lineas[0].strip().split(": ")[1]
                contrasena = lineas[1].strip().split(": ")[1]
                return usuario, contrasena
    except IOError:
        pass
    return None, None

# Cargar el login almacenado (si existe)
usuario, contrasena = cargar_login()

if usuario and contrasena:
    print("Iniciando sesión automáticamente con el siguiente usuario:")
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {contrasena}")
    print("Sesion restaurada exitosamente...")
else:
    # Si no se encuentra un login almacenado, solicitar credenciales al usuario
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Guardar las credenciales en el archivo
    guardar_login(usuario, contrasena)
    print("Login guardado exitosamente...")

