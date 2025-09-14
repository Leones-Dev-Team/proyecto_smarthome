# ui_usuarios_estandar.py

from modulos.servicios import servicios_usuarios_estandar as su
from modulos.datos.datos_dispositivos import dispositivos
from modulos.ui.ui_utils import obtener_input, pausar_pantalla


def registrar_usuario():
    """Crea un nuevo usuario estándar."""
    print("\n--- Registrar Nuevo Usuario ---")
    nombre = obtener_input("Elige un nombre de usuario: ").lower()
    contraseña = obtener_input("Elige una contraseña: ")
    id_hogar = obtener_input("ID del hogar: ")

    edad = obtener_input("Edad: ", int)
    mail = obtener_input("Correo electrónico: ")
    telefono = obtener_input("Teléfono: ")

    if su.registrar_usuario(nombre, contraseña, id_hogar, edad, mail, telefono):
        print(f"¡Usuario '{nombre}' registrado con éxito! ")
    else:
        print("Ese usuario ya existe o el hogar no existe.")
    pausar_pantalla()


def iniciar_sesion():
    """Permite entrar al sistema. Devuelve usuario y rol si es correcto."""
    print("\n--- Iniciar Sesión ---")
    nombre = obtener_input("Usuario: ")
    if nombre is not None:
        nombre = nombre.lower()
    contra = obtener_input("Contraseña: ")

    usuario, rol = su.iniciar_sesion(nombre, contra)
    if usuario:
        print(f"¡Bienvenido/a, {nombre}! (Rol: {rol})")
        return {"usuario": usuario, "rol": rol}
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return {"usuario": None, "rol": None}


def menu_estandar(nombre_usuario):
    """Muestra opciones para usuarios estándar."""
    while True:
        print(f"\n--- Menú Estándar ({nombre_usuario}) ---")
        print("""
        1. Ver mis datos
        2. Activar/Ejecutar automatización
        3. Consultar dispositivos
        0. Cerrar sesión
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            info = su.obtener_info_usuario(nombre_usuario)
            if info:
                print("\n--- Tus Datos ---")
                print(f"Usuario: {info['nombre']}")
                print(f"Rol: {info['rol']}")
                print(f"ID Hogar: {info.get('id_hogar')}")
                print(f"Edad: {info.get('edad')}")
                print(f"Correo electrónico: {info.get('mail')}")
                print(f"Teléfono: {info.get('telefono')}")
            else:
                print("No se encontró la información del usuario.")
            pausar_pantalla()

        elif opcion == '2':
            print("\n--- Automatización ---\n¡Automatización predefinida activada! ")
            pausar_pantalla()

        elif opcion == '3':
            print("\n--- Dispositivos ---")
            if not dispositivos:
                print("No hay dispositivos conectados.")
            else:
                for d in dispositivos:
                    print(
                        f"ID: {d['id_dispositivo']}, Tipo: {d['tipo_dispositivo']}, Estado: {d['estado']}, "
                        f"Esencial: {'Sí' if d['es_esencial'] else 'No'}, "
                        f"Usuario Conectado: {d.get('id_usuario_conectado', '-')}, "
                        f"Ubicación: {d.get('ubicacion', '-')}, "
                        f"Marca: {d.get('marca_dispositivo', '-')}, "
                        f"Consumo: {d.get('consumo_energetico', '-')}W"
                    )
            pausar_pantalla()

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}. ")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_principal_usuarios_estandar():
    """El menú principal de gestión de usuarios estándar."""
    while True:
        print("""
        --- Menú de Usuarios Estándar ---
        1. Registrar nuevo usuario
        2. Iniciar sesión
        0. Volver al menú global
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            return iniciar_sesion()
        elif opcion == '0':
            print("Saliendo del menú de usuarios estándar.")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 0.")
