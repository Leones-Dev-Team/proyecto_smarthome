# modulos/ui/ui_usuarios.py

from modulos.servicios import servicios_usuarios as su
from modulos.datos.datos_dispositivos import dispositivos
from modulos.ui.ui_dispositivos import menu_principal_dispositivos


def obtener_input(mensaje):
    """Pide al usuario que escriba algo y lo devuelve limpio."""
    return input(mensaje).strip()


def pausar_pantalla():
    """Espera que el usuario presione Enter."""
    input("\nPresiona Enter para continuar...")


def registrar_usuario():
    """Crea un nuevo usuario estándar."""
    print("\n--- Registrar Nuevo Usuario ---")
    nombre = obtener_input("Elige un nombre de usuario: ").lower()
    contraseña = obtener_input("Elige una contraseña: ")
    id_hogar = obtener_input("ID del hogar: ")

    # Validación básica de edad
    while True:
        edad = obtener_input("Edad: ")
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("La edad debe ser un número válido.")

    mail = obtener_input("Correo electrónico: ")
    telefono = obtener_input("Teléfono: ")

    if su.registrar_usuario(nombre, contraseña, id_hogar, edad, mail, telefono):
        print(f"¡Usuario '{nombre}' registrado con éxito!")
    else:
        print("Ese usuario ya existe. Elige otro nombre.")
    pausar_pantalla()


def iniciar_sesion():
    """Permite entrar al sistema. Devuelve usuario y rol si es correcto."""
    print("\n--- Iniciar Sesión ---")
    nombre = obtener_input("Usuario: ").lower()
    contra = obtener_input("Contraseña: ")

    usuario, rol = su.iniciar_sesion(nombre, contra)
    if usuario:
        print(f"¡Bienvenido/a, {nombre}!")
        return usuario, rol
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return None, None


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
            print("\n--- Automatización ---\n¡Automatización predefinida activada!")
            pausar_pantalla()

        elif opcion == '3':
            print("\n--- Dispositivos ---")
            if not dispositivos:
                print("No hay dispositivos conectados.")
            else:
                for d in dispositivos:
                    print(
                        f"ID: {d['id']}, Tipo: {d['tipo']}, Estado: {d['estado']}, "
                        f"Esencial: {'Sí' if d['es_esencial'] else 'No'}, "
                        f"Usuario Conectado: {d.get('id_usuario_conectado','-')}, "
                        f"Ubicación: {d.get('ubicacion','-')}, "
                        f"Marca: {d.get('marca_dispositivo','-')}, "
                        f"Consumo: {d.get('consumo_energetico','-')}W"
                    )
            pausar_pantalla()

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_administrador(nombre_usuario):
    """Muestra opciones para usuarios administradores."""
    while True:
        print(f"\n--- Menú Administrador ({nombre_usuario}) ---")
        print("""
        1. Consultar automatizaciones activas
        2. Gestionar dispositivos
        3. Modificar rol de un usuario
        0. Cerrar sesión
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            print("\n--- Automatizaciones Activas ---\nMostrando automatizaciones en curso.")
            pausar_pantalla()

        elif opcion == '2':
            menu_principal_dispositivos(dispositivos, volver_a=menu_administrador)

        elif opcion == '3':
            usuario_a_modificar = obtener_input("Usuario para cambiar su rol: ").lower()
            nuevo_rol = obtener_input("Nuevo rol (estándar/administrador): ").lower()
            if su.cambiar_rol(usuario_a_modificar, nuevo_rol):
                print(f"¡Rol de '{usuario_a_modificar}' cambiado a '{nuevo_rol}'!")
            else:
                print("Usuario no encontrado o rol inválido.")
            pausar_pantalla()

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_principal_usuarios():
    """El menú principal de gestión de usuarios."""
    while True:
        print("""
        --- Menú de Usuarios ---
        1. Registrar nuevo usuario
        2. Iniciar sesión
        0. Volver al menú global
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario_actual, rol_actual = iniciar_sesion()
            if usuario_actual:
                if rol_actual == "estandar":
                    menu_estandar(usuario_actual)
                elif rol_actual == "administrador":
                    menu_administrador(usuario_actual)
        elif opcion == '0':
            print("Saliendo del menú de usuarios.")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 0.")
